# portal/urls.py
from django.conf.urls import url, include
from portal.views import views

# We are adding a URL called /home

urlpatterns = [
    url(r'^$', views.home),

    url(r'^models/', include([
        url(r'^linear_regression/', views.linear_regression),
    ])),

    url(r'^dashboard/', views.dashboard),
]
