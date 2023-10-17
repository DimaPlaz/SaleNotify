from config import settings
from dtos.game import RemoveSubscription, CreateSubscription, Game
from logger.logger import get_logger
from repositories.client_repository import TortoiseClientRepository
from repositories.game_repository import TortoiseGameRepository
from repositories.interfaces import BaseSubscriptionRepository, BaseSteamRepository, BaseGameRepository, \
    BaseClientRepository
from repositories.steam_repository import SteamRepository
from repositories.subscription_repository import TortoiseSubscriptionRepository
from services.interfaces import SubscriptionServiceI, NotifierI
from exceptions.steam import (SteamBadProfileUrlError,
                              SteamEmptyWishlistError,
                              SteamWishlistWithoutPaidGamesError)
from services.notifier import NotifierServiceFactory

logger = get_logger()


class SubscriptionService(SubscriptionServiceI):
    def __init__(self,
                 subscription_repository: BaseSubscriptionRepository,
                 game_repository: BaseGameRepository,
                 steam_repository: BaseSteamRepository,
                 client_repository: BaseClientRepository,
                 notifier_service: NotifierI):
        self._client_repository = client_repository
        self._notifier_service = notifier_service
        self._subscription_repository = subscription_repository
        self._game_repository = game_repository
        self._steam_repository = steam_repository

    async def subscribe(self, create_subscription: CreateSubscription):
        return await self._subscription_repository.subscribe(create_subscription)

    async def unsubscribe(self, remove_subscription: RemoveSubscription):
        return await self._subscription_repository.unsubscribe(remove_subscription)

    async def get_games_subscribed(self, client_id: int) -> list[Game]:
        return await self._subscription_repository.get_games_subscribed(client_id)

    async def delete_games_subscribed(self, client_id: int):
        return await self._subscription_repository.delete_client_subscriptions(client_id)

    async def subscribe_to_games_from_wishlist(self, client_id: int, steam_profile_url: str):
        client = await self._client_repository.get_clients_by_id(client_id)
        try:
            steam_ids = await self._steam_repository.get_wishlist_by_profile_url(steam_profile_url)
            subs = await self._subscription_repository.get_client_subscriptions(client_id)
            subs_game_ids = list(map(lambda sub: sub.game_id, subs))
            games = await self._game_repository.get_games_by_steam_ids_without_subs(steam_ids, subs_game_ids)
            game_ids = list(map(lambda game: game.id, games))
            await self._subscription_repository.bulk_subscribe(client_id, game_ids)
            message = ("Your wishlist has been synced successfully\n"
                       "You can check the list of subscriptions")
            await self._notifier_service.send_message(client.chat_id, message)
        except (SteamBadProfileUrlError,
                SteamEmptyWishlistError,
                SteamWishlistWithoutPaidGamesError) as err:
            await self._notifier_service.send_message(client.chat_id, err.message)
        except Exception as err:
            await logger.error(err)
            message = "There was an error parsing your wishlist, please try later"
            await self._notifier_service.send_message(client.chat_id, message)


class SubscriptionServiceFactory:
    @classmethod
    def get_service(cls):
        return SubscriptionService(
            TortoiseSubscriptionRepository(),
            TortoiseGameRepository(),
            SteamRepository(
                settings.STEAM_SEARCH_URL,
                settings.STEAM_WISHLIST_URL
            ),
            TortoiseClientRepository(),
            NotifierServiceFactory.get_service()
        )
