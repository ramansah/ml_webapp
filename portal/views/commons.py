from abc import abstractmethod
import pickle
from portal import mongo


class BaseLearningModel:

    NEW_MODEL = 'new_model'
    STATUS_ENQUIRY = 'status_enquiry'
    PREDICT = 'predict'
    DELETE = 'delete'

    def __init__(self, user_id, post):

        self.model = None
        self.user_id = user_id
        self.post = post
        self.name = post.get('name')
        self.model_id = post.get('model_id')
        self.action = post.get('action')
        self.response = None

        self.check_status()

        if self.model_id is not None and self.action != BaseLearningModel.NEW_MODEL:
            self.load_from_db()

        if self.action in (BaseLearningModel.NEW_MODEL, BaseLearningModel.PREDICT):
            self.check_input()
            if self.action == BaseLearningModel.NEW_MODEL:
                self.save_to_db()
                self.response = dict(status='Training under progress', model_id=self.model_id)
                self.train()
                self.save_to_db()
                self.response = dict(status='Trained', model_id=self.model_id)
            elif self.action == BaseLearningModel.PREDICT:
                self.load_from_db()
                self.predict()

    def check_status(self):
        if self.action not in (
                BaseLearningModel.NEW_MODEL, BaseLearningModel.STATUS_ENQUIRY,
                BaseLearningModel.PREDICT, BaseLearningModel.DELETE):
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
        model = mongo.BaseModel.objects(id=self.model_id)[0]
        self.model = pickle.loads(model.data)

    def save_to_db(self):
        data = pickle.dumps(self.model)

        if self.model_id:
            model = mongo.BaseModel.objects(id=self.model_id)[0]
            model.data = data
            model.save()

        else:
            model = mongo.BaseModel(
                name=self.name,
                data=data
            )
            model.save()
            self.model_id = str(model.id)


class ModelException(Exception):
    def __init__(self, message, *args):
        Exception.__init__(self, *args)
        self.message = message

    def get_message(self):
        return self.message
