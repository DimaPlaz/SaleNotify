import json
import re
from asyncio import sleep

from bs4 import BeautifulSoup
import httpx
from httpx import ReadTimeout

from config import settings
from dtos.game import Game
from logger.logger import get_logger
from repositories.interfaces import BaseSteamRepository


logger = get_logger()


class SteamRepository(BaseSteamRepository):
    def __init__(self, search_url: str = settings.STEAM_SEARCH_URL):
        self.search_url = search_url

    @staticmethod
    def __parse_response(content) -> list[Game]:
        games = []

        bs = BeautifulSoup(content)

        for block in bs.find_all("a", class_="search_result_row"):
            title = block.find_all("span", class_="title")[0].text
            discount_block = block.select('div.discount_block:not(.no_discount)')
            image = block.find_all("img")[0]
            image_link: str = image["srcset"].split(" ")[-2].split("?")[0]
            image_link = image_link[:image_link.rfind("/")] + "/header.jpg"
            store_link = block["href"].split("?")[0]
            steam_id = block["data-ds-itemkey"]
            discount = int(discount_block[0].get("data-discount")) if discount_block else 0
            search_field = re.sub("[^A-Za-z0-9]+", "", title).lower()
            span = block.find('span', class_='search_review_summary')
            try:
                data_tooltip_html = span['data-tooltip-html']
                review_count = int(re
                                   .compile(r"(?<=of the )[\d,]+")
                                   .search(data_tooltip_html)
                                   .group()
                                   .replace(",", ""))
            except TypeError:
                review_count = 0

            games.append(
                Game(
                    name=title,
                    search_field=search_field,
                    review_count=review_count,
                    discount=discount,
                    image_link=image_link,
                    store_link=store_link,
                    steam_id=steam_id
                )
            )

        return games

    async def get_games(self) -> list[Game]:
        params = {
            "start": 0,
            "count": settings.STEAM_SEARCH_COUNT,
            "sort_by": "_ASC",
            "infinite": 1,
            "force_infinite": 1,
            "category1": 998,
            "hidef2p": 1,
            "ndl": 1,
            "ignore_preferences": 1,
            "cc": "kz"
        }
        while True:
            try:
                async with httpx.AsyncClient() as client:
                    r = await client.get(self.search_url, params=params)
                    if r.status_code != 200:
                        await logger.debug(f"error on steam server: {r.content}")
                        await sleep(60)
                        continue

                    content = r.json()
                    yield self.__parse_response(content["results_html"])
                    if params["start"] >= content["total_count"]:
                        break

                    params["start"] += settings.STEAM_SEARCH_COUNT
                    await logger.debug(f"downloaded {params['start']} "
                                       f"out of {content['total_count']}")
            except (httpx.ConnectTimeout,
                    httpx.ConnectError,
                    json.decoder.JSONDecodeError,
                    TimeoutError,
                    ReadTimeout) as err:
                await logger.debug(f"error getting games from steam: {err}")
                await sleep(10)
                continue
