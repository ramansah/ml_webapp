import json
from abc import abstractmethod
import pickle
from django.http import JsonResponse
from portal import mongo


class BaseViewModel:

    NEW_MODEL = 'new_model'
    STATUS_ENQUIRY = 'status_enquiry'
    PREDICT = 'predict'
    DELETE = 'delete'

    def __init__(self, user_id, post):

        self.model = None
        self.user_id = user_id
        self.post = json.loads(post)
        self.name = post.get('name')
        self.model_id = post.get('model_id')
        self.action = post.get('action')
        self.response = None

        self.check_status()

        if self.model_id is not None and self.action != BaseViewModel.NEW_MODEL:
            self.load_from_db()

        if self.action in (BaseViewModel.NEW_MODEL, BaseViewModel.PREDICT):
            self.check_input()
            if self.action == BaseViewModel.NEW_MODEL:
                self.save_to_db()
                self.response = dict(status='Training under progress', model_id=self.model_id)
                self.train()
                self.save_to_db()
                self.response = dict(status='OK')
            elif self.action == BaseViewModel.PREDICT:
                self.predict()

    def check_status(self):
        if self.action not in (
                BaseViewModel.NEW_MODEL, BaseViewModel.STATUS_ENQUIRY,
                BaseViewModel.PREDICT, BaseViewModel.DELETE):
            raise ModelException(message='Invalid action. Please fill a valid action and try again')

    @abstractmethod
    def check_input(self):
        pass

    @abstractmethod
    def predict(self):
        pass

    @abstractmethod
    def train(self):
        pass

    def load_from_db(self):
        user = mongo.ModelList.objects(user_id=self.user_id)[0]
        for model in user.models:
            if self.model_id == model.id:
                self.model = pickle.loads(model.data)
                return

    def save_to_db(self):
        data = pickle.dumps(self.model)
        user = mongo.ModelList.objects(user_id=self.user_id)
        if user is None:
            user = mongo.ModelList(user_id=self.user_id)
        else:
            user = user[0]

        model = mongo.BaseModel(
            name=self.name,
            data=data
        )
        user.models.append(model)
        user.save()
        self.model_id = model.id


class ModelException(Exception):
    def __init__(self, message, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.message = message

    def get_message(self):
        return self.message
