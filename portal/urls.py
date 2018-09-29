from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from portal.views import views
from portal.views.api import GenericModelController


urlpatterns = [
    url(r'^$', views.home),

    url(r'^api/', include([
        url(r'^login/', obtain_jwt_token),
        url(r'^model/', GenericModelController.as_view()),
    ])),

    url(r'^dashboard/', views.dashboard),
    url(r'^delete_model/', views.delete_model),
]
