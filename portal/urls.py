from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from portal.views import views, api


urlpatterns = [
    url(r'^$', views.home),

    url(r'^api/', include([
        url(r'^login/', obtain_jwt_token),
        url(r'^linear_regression/', api.LinearRegression.as_view()),
        url(r'^knn_classifier/', api.KNearestNeighbors.as_view()),
        url(r'^svm_classifier/', api.SVMClassifier.as_view()),
    ])),

    url(r'^models/', include([
        url(r'^linear_regression/', views.linear_regression),
        url(r'^knn_classifier/', views.knn_classifier),
        url(r'^svm_classifier/', views.svm_classifier),
    ])),

    url(r'^dashboard/', views.dashboard),
    url(r'^delete_model/', views.delete_model),
]
