from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'GET':
        context = dict()
        return render(request, 'signup.html', context)

    elif request.method == 'POST':
        try:
            user = User.objects.create_user(
                username=request.POST.get('username'),
                password=request.POST.get('password'),
                email=request.POST.get('email')
            )
            if user is not None:
                return redirect('/login')
        except Exception:
            pass

        context = dict(
            error='User Registration Failed. Username and Email are unique.'
        )
        return render(request, 'signup.html', context)