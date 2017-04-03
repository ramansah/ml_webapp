# portal/urls.py
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token

from portal.views import views, api

# We are adding a URL called /home

urlpatterns = [
    url(r'^$', views.home),

    url(r'^api/', include([
        url(r'^login/', obtain_jwt_token),
        url(r'^linear_regression/', api.LinearRegression.as_view())
    ])),

    url(r'^models/', include([
        url(r'^linear_regression/', views.linear_regression),
    ])),

    url(r'^dashboard/', views.dashboard),
]
