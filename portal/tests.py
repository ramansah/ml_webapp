import json

from django.contrib.auth.models import User
from django.test import TestCase
from portal.views.views import linear_regression
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
        self.c = Client()
        self.c.login(username=username, password=password)

    def test_model(self):
        self.step_one_create_model()

    def step_one_create_model(self):
        request = {
            'action': 'new_model',
            'name': 'My Linear Regression Model 1',
            'input_x': [[1, 2], [2, 1], [2, 3]],
            'input_y': [5, 4, 8]
        }
        response = self.c.post(
            path='/models/linear_regression/',
            content_type='application/json',
            data=json.dumps(request)
        )
        print(response)
