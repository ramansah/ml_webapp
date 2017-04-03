from rest_framework.response import Response
from rest_framework.views import APIView
from portal.views import linear_regression
from portal.views.commons import ModelException


class LinearRegression(APIView):
    def post(self, request):
        try:
            model = linear_regression.LinearRegression(
                user_id=request.user.id,
                post=request.data
            )
            return Response(model.response)
        except ModelException as e:
            return Response(dict(status='Error', message=e.get_message()))
