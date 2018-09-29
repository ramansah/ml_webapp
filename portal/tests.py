import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client


class LinearModelTest(TestCase):

    def setUp(self):
        username = 'testUser'
        password = 'password'
        user = User.objects.create_user(
            username=username,
            password=password,
            email='test@test.com'
        )
        self.assertIsNotNone(user)
        self.user_id = user.id
        self.client = Client()
        self.client.login(username=username, password=password)

    def test_model(self):
        self.step_one_create_model()
        self.step_two_predict_model()

    def step_one_create_model(self):
        request = {
            'model_path': 'sklearn.linear_model.LinearRegression',
            'action': 'new_model',
            'name': 'My Linear Regression Model',
            'input_x': [[1, 2], [2, 1], [2, 3]],
            'input_y': [5, 4, 8]
        }
        response = self.post_data_on_model_endpoint(request)
        self.assertEqual(response.get('status'), 'Trained')
        self.model_id = response.get('model_id')

    def step_two_predict_model(self):
        request = {
            'model_id': self.model_id,
            'action': 'predict',
            'input_x': [[5, 10]],
        }
        response = self.post_data_on_model_endpoint(request)
        self.assertEqual(response.get('status'), 'OK')
        answer = int(response.get('prediction')[0])
        self.assertEqual(answer, 25)

    def post_data_on_model_endpoint(self, request):
        response = self.client.post(
            path='/api/model/',
            content_type='application/json',
            data=json.dumps(request)
        )
        return json.loads(response.content.decode('utf-8'))
