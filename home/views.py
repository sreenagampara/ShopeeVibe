from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import contactform
from .models import register
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/home-page')
        else:
            messages.info(request, "Invalid User Name Or Password")
            return redirect('/home')
    else:
        return render(request, 'login.html')


def creat(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # print(username)
        register.objects.create(username=username, password=password, email=email)
        print('user created')
        return redirect('/home')
    else:

        return render(request, 'creat-new.html')


def homepage(request):
    return render(request, 'home page.html')


def orderform(request):
    return render(request, 'oder form.html')


def orderplaced(request):
    return render(request, 'oredr placed.html')
