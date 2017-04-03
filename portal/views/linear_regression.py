from portal.views.commons import BaseLearningModel, ModelException
from sklearn import linear_model


class LinearRegression(BaseLearningModel):

    def __init__(self, user_id, post):
        super().__init__(user_id=user_id, post=post, model_type='Linear Regression')

    def predict(self):
        prediction = self.model.predict(X=self.post.get('input_x'))
        self.response = dict(status='OK', prediction=prediction)

    def train(self):
        self.model = linear_model.LinearRegression()
        self.model.fit(self.post.get('input_x'), self.post.get('input_y'))
        self.response = dict(status='Trained')

    def check_input(self):
        input_x = self.post.get('input_x')
        if not input_x:
            raise ModelException('input_x empty')
        if self.action == BaseLearningModel.NEW_MODEL:
            input_y = self.post.get('input_y')
            if not input_y:
                raise ModelException('input_y empty')
