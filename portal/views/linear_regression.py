from portal.views.commons import BaseViewModel, ModelException


class LinearRegression(BaseViewModel):

    def __init__(self, user_id, post):
        super().__init__(user_id=user_id, post=post)

    def predict(self):
        pass

    def train(self):
        pass

    def check_input(self):
        input_x = self.post.get('input_x')
        if not input_x:
            raise ModelException('input_x empty')
        input_y = self.post.get('input_y')
        if not input_y:
            raise ModelException('input_y empty')
