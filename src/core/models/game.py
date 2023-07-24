from tortoise import fields, models


class GameModel(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64, unique=True, null=False)
    discount = fields.SmallIntField(default=0)
    image_link = fields.CharField(max_length=256, unique=True, null=False)
    store_link = fields.CharField(max_length=256, unique=True, null=False)

    class Meta:
        table = "games"
