"""ml_webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# ml_webapp/urls.py
from django.conf.urls import include, url
from django.contrib.auth import views
from portal.forms import LoginForm
from ml_webapp import basic_views


urlpatterns = [
    url(r'', include('portal.urls')),
    url(r'^login/$', views.LoginView.as_view(), {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', views.LogoutView.as_view(), {'next_page': '/login'}),
    url(r'^signup/$', basic_views.signup),
]
