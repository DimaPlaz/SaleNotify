from core.models import GameSubscriptionModel
from dtos.factories import SubscriptionFactory
from dtos.game import Subscription, RemoveSubscription, CreateSubscription
from repositories.interfaces import BaseSubscriptionsRepository


class TortoiseSubscriptionsRepository(BaseSubscriptionsRepository):
    async def subscribe(self, sub: CreateSubscription):
        model = await GameSubscriptionModel.create(client_id=sub.client_id, game_id=sub.game_id)
        return SubscriptionFactory.model_to_dto(model)

    async def unsubscribe(self, unsub: RemoveSubscription):
        await GameSubscriptionModel.filter(client_id=unsub.client_id, game_id=unsub.game_id).delete()

    async def get_client_subscriptions(self, client_id: int) -> list[Subscription]:
        models = await GameSubscriptionModel.filter(client_id=client_id).all()
        return SubscriptionFactory.models_to_dtos(models)
