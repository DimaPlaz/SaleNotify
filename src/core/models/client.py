from tortoise import fields, models


class ClientModel(models.Model):
    id = fields.IntField(pk=True)
    user = fields.CharField(max_length=64, unique=True, null=False)

    class Meta:
        table = "clients"
