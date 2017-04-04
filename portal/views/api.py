from rest_framework.response import Response
from rest_framework.views import APIView
from portal.views import learning_models
from portal.views.commons import ModelException


class LinearRegression(APIView):
    def post(self, request):
        try:
            model = learning_models.LinearRegression(
                user_id=request.user.id,
                post=request.data
            )
            return Response(model.response)
        except ModelException as e:
            return Response(dict(status='Error', message=e.get_message()))


class KNearestNeighbors(APIView):
    def post(self, request):
        try:
            model = learning_models.KNNClassifier(
                user_id=request.user.id,
                post=request.data
            )
            return Response(model.response)
        except ModelException as e:
            return Response(dict(status='Error', message=e.get_message()))
