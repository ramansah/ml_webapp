from rest_framework.response import Response
from rest_framework.views import APIView
from portal.views.generic_model import BaseLearningModel
from portal.views.utils import api_decorator


class GenericModelController(APIView):
    @api_decorator
    def post(self, request):
        model = BaseLearningModel(
            user_id=request.user.id,
            params=request.data
        )
        return Response(model.response)
