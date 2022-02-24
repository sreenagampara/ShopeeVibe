from django.shortcuts import render
from django.http import HttpResponse
from .form import contactform


# Create your views here.

def home(request):
    return render(request, 'login.html')


def creat(request):
    return render(request, 'creat-new.html')
