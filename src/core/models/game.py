from tortoise import fields, models


class GameModel(models.Model):
    id = fields.IntField(pk=True)
    steam_id = fields.CharField(max_length=32, unique=True)
    name = fields.CharField(max_length=512, null=False)
    search_field = fields.CharField(max_length=512, null=False, default='')
    review_count = fields.IntField(null=False, default=0)
    discount = fields.SmallIntField(default=0)
    image_link = fields.CharField(max_length=512, unique=False, null=False)
    store_link = fields.CharField(max_length=512, unique=True, null=False)

    class Meta:
        table = "games"
