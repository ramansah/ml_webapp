import pickle

from mongoengine import ValidationError
from portal import mongo
from portal.exceptions import ModelException


class BaseLearningModel:

    NEW_MODEL = 'new_model'
    STATUS_ENQUIRY = 'status'
    PREDICT = 'predict'
    DELETE = 'delete'

    def __init__(self, user_id, params):

        self.model = None
        self.user_id = user_id
        self.post = params
        self.model_path = params.get('model_path')
        self.name = params.get('name')
        self.model_id = params.get('model_id')
        self.action = params.get('action')
        self.response = None

        self.check_status()

        if self.model_id is not None and self.action != BaseLearningModel.NEW_MODEL:
            self.load_from_db()

        if self.action in (BaseLearningModel.NEW_MODEL, BaseLearningModel.PREDICT):
            self.check_input()
            if self.action == BaseLearningModel.NEW_MODEL:
                if not self.name:
                    raise ModelException('Name not defined')
                self.save_to_db()
                self.response = dict(status='Training under progress', model_id=self.model_id)
                # TODO Make self.train() a Celery task
                self.train()
                self.save_to_db()
                self.response = dict(status='Trained', model_id=self.model_id)
            elif self.action == BaseLearningModel.PREDICT:
                self.load_from_db()
                self.predict()

        elif self.action == BaseLearningModel.DELETE:
            if not self.model_id:
                raise ModelException('Model ID not present')
            self.delete()

    def check_status(self):

        if self.action not in (
                BaseLearningModel.NEW_MODEL, BaseLearningModel.STATUS_ENQUIRY,
                BaseLearningModel.PREDICT, BaseLearningModel.DELETE):
            raise ModelException(message='Invalid action. Please fill a valid action and try again')

    def check_input(self):

        input_x = self.post.get('input_x')
        if not input_x:
            raise ModelException('input_x empty')
        if self.action == BaseLearningModel.NEW_MODEL:
            input_y = self.post.get('input_y')
            if not input_y:
                raise ModelException('input_y empty')

    def predict(self):

        prediction = self.model.predict(X=self.post.get('input_x'))
        self.response = dict(status='OK', prediction=prediction)

    def train(self):

        family_path = '.'.join(self.model_path.split('.')[0:-1])
        family_name = self.model_path.split('.')[1]
        model_name = self.model_path.split('.')[-1]
        parent_module = __import__(family_path)
        model_family = getattr(parent_module, family_name)
        model_constructor = getattr(model_family, model_name)
        self.model = model_constructor()
        x = self.post.get('input_x')
        y = self.post.get('input_y')
        self.model.fit(x, y)
        self.response = dict(status='Trained')

    def load_from_db(self):
        try:
            model = mongo.BaseModel.objects(id=self.model_id)[0]
            self.model = pickle.loads(model.data)
        except ValidationError:
            raise ModelException('Invalid Object ID')
        except Exception:
            raise ModelException('Object ID not present in DB. Are you sure you didn\'t delete the model')

    def save_to_db(self):

        data = pickle.dumps(self.model)

        if self.model_id:
            model = mongo.BaseModel.objects(id=self.model_id)[0]
            model.data = data
            model.save()

        else:
            model = mongo.BaseModel(
                name=self.name,
                user_id=self.user_id,
                model_path=self.model_path,
                data=data
            )
            model.save()
            self.model_id = str(model.id)

    def delete(self):

        model = mongo.BaseModel.objects(id=self.model_id)[0]
        model.delete()
        self.response = dict(
            status='Deleted Model Successfully'
        )
