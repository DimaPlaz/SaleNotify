from tortoise import fields, models


class GameModel(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=512, unique=True, null=False)
    discount = fields.SmallIntField(default=0)
    image_link = fields.CharField(max_length=512, unique=False, null=False)
    store_link = fields.CharField(max_length=512, unique=True, null=False)

    class Meta:
        table = "games"
