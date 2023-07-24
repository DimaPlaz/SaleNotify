from asyncio import sleep

from bs4 import BeautifulSoup
import httpx

from config import settings
from dtos.game import Game
from repositories.interfaces import BaseSteamRepository


class SteamRepository(BaseSteamRepository):
    def __init__(self, search_url: str = settings.STEAM_SEARCH_URL):
        self.search_url = search_url

    @staticmethod
    def __parse_response(content) -> list[Game]:
        games = []

        bs = BeautifulSoup(content)

        for block in bs.find_all("a", class_="search_result_row"):
            title = block.find_all("span", class_="title")[0]
            discount_block = block.find_all("div", class_="discount_block")
            image = block.find_all("img")[0]

            games.append(
                Game(
                    name=title.text,
                    discount=discount_block[0].get("data-discount") if discount_block else 0,
                    image_link=image["srcset"].split(" ")[-2],
                    store_link=block["href"],
                )
            )

        return games

    async def get_games(self) -> list[Game]:
        games: list[Game] = []
        params = {
            "start": 0,
            "count": settings.STEAM_SEARCH_COUNT,
            "sort_by": "_ASC",
            "supportedlang": "english",
            "infinite": 1
        }
        while True:
            async with httpx.AsyncClient() as client:
                r = await client.get(self.search_url, params=params)
                if r.status_code != 200:
                    await sleep(60)
                    continue

                content = r.json()
                games.extend(self.__parse_response(content["results_html"]))
                if params["start"] >= content["total_count"]:
                    break

                params["start"] += settings.STEAM_SEARCH_COUNT
        return games

