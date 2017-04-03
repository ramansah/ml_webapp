from mongoengine import Document, BinaryField, EmbeddedDocument, IntField, ListField, EmbeddedDocumentField, connect
from mongoengine import StringField


class BaseModel(Document):
    user_id = IntField()
    name = StringField(required=True)
    data = BinaryField()
    meta = {
        'allow_inheritance': True
    }

