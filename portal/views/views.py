from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from portal.mongo import BaseModel


def home(request):
    return render(request, "home.html")


def about_us(request):
    if request.method == 'GET':
        return render(request, 'about_us.html', context=None)


@login_required
def dashboard(request):
    if request.method == 'GET':
        user_id = request.user.id
        mongo_models = BaseModel.objects(user_id=user_id)
        context = dict(
            my_models=mongo_models
        )
        return render(request, 'dashboard.html', context)


@login_required
def delete_model(request):
    if request.method == 'GET':
        model_id = request.GET.get('model_id')
        model = BaseModel.objects(id=model_id)[0]
        model.delete()
        return redirect('/dashboard/')
