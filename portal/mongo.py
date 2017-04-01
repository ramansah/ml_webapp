from mongoengine import Document, BinaryField, EmbeddedDocument, IntField, ListField, EmbeddedDocumentField, connect
from mongoengine import StringField


class BaseModel(EmbeddedDocument):
    name = StringField(required=True)
    data = BinaryField()
    meta = {
        'allow_inheritance': True
    }


class ModelList(Document):
    user_id = IntField()
    models = ListField(EmbeddedDocumentField(BaseModel))
    meta = {
        'indexes': ['user_id']
    }

connect(db='ML_WEB_APP')
