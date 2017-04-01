from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from portal.views.linear_regression import LinearRegression


def home(request):
    return render(request, "home.html")


@login_required
def dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard.html', context=None)


@login_required
def linear_regression(request):
    if request.method == 'GET':
        return render(request, 'models/linear_regression.html', context=None)
    elif request.method == 'POST':
        print(request.POST)
        return
        model = LinearRegression(
            user_id=request.user.id,
            post=request.POST.body
        )
        return JsonResponse(model.response)
