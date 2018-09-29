import datetime
import mongoengine


class BaseModel(mongoengine.Document):

    meta = {
        'allow_inheritance': True,
        'indexes': [
            'user_id'
        ]
    }

    user_id = mongoengine.IntField()
    name = mongoengine.StringField(required=True)
    model_path = mongoengine.StringField(required=True)
    data = mongoengine.BinaryField()
    created_at = mongoengine.DateTimeField()
    updated_at = mongoengine.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)
