from tortoise import fields, models


class GameSubscriptionModel(models.Model):
    id = fields.IntField(pk=True)
    client: fields.ForeignKeyRelation = fields.ForeignKeyField("core.ClientModel", related_name="subscriptions")
    game: fields.ForeignKeyRelation = fields.ForeignKeyField("core.GameModel", related_name="subscriptions")

    class Meta:
        table = "subscriptions"
