from tortoise import Model, fields


class SupportMessage(Model):
    id = fields.BigIntField(pk=True)
    chat_id = fields.BigIntField(null=False)
