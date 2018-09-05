from rest_framework.response import Response
from rest_framework.views import APIView
from portal.views import learning_models
from portal.views.utils import api_decorator


class LinearRegression(APIView):
    @api_decorator
    def post(self, request):
        model = learning_models.LinearRegression(
            user_id=request.user.id,
            post=request.data
        )
        return Response(model.response)


class KNearestNeighbors(APIView):
    @api_decorator
    def post(self, request):
        model = learning_models.KNNClassifier(
            user_id=request.user.id,
            post=request.data
        )
        return Response(model.response)


class SVMClassifier(APIView):
    @api_decorator
    def post(self, request):
        model = learning_models.SVMClassifier(
            user_id=request.user.id,
            post=request.data
        )
        return Response(model.response)

