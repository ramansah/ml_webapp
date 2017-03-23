from django.shortcuts import render

# Create your views here.
#portal/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating


def home(request):
    return render(request, "home.html")


@login_required
def dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard.html', context=None)


@login_required
def linear_regression(request):
    if request.method == 'GET':
        return render(request, 'linear_regression.html', context=None)


@login_required
def dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard.html', context=None)
