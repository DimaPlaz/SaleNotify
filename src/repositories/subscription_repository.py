from core.models import GameSubscriptionModel, GameModel
from dtos.client import Client
from dtos.factories import SubscriptionFactory, GameFactory
from dtos.game import Subscription, RemoveSubscription, CreateSubscription, Game
from repositories.interfaces import BaseSubscriptionRepository


class TortoiseSubscriptionRepository(BaseSubscriptionRepository):
    async def subscribe(self, sub: CreateSubscription):
        model = await GameSubscriptionModel.create(client_id=sub.client_id, game_id=sub.game_id)
        return SubscriptionFactory.model_to_dto(model)

    async def unsubscribe(self, unsub: RemoveSubscription):
        await GameSubscriptionModel.filter(client_id=unsub.client_id, game_id=unsub.game_id).delete()

    async def get_client_subscriptions(self, client_id: int) -> list[Subscription]:
        models = await GameSubscriptionModel.filter(client_id=client_id).all()
        return SubscriptionFactory.models_to_dtos(models)

    async def get_games_subscribed(self, client_id: int) -> list[Game]:
        models = await GameModel.filter(subscriptions__client_id=client_id).all()
        return GameFactory.models_to_dtos(models)

    async def delete_client_subscriptions(self, client_id: int):
        await GameSubscriptionModel.filter(client_id=client_id).delete()
