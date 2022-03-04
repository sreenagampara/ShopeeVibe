from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import contactform
from .models import register, product, cart
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.

def home(request):
    x = "User Name Or Password Is Invalid"
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')
        # print(username)
        # print(password)
        user = auth.authenticate(username=username, password=password)
        # print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('/home-page')
        else:
            messages.info(request, "Invalid User Name Or Password")
        return render(request, 'login.html', {'message': x})
    else:
        return render(request, 'login.html')


def creat(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # print(username)
        user = User.objects.create_user(username=username, password=password, email=email)
        print('user created')
        return redirect('/home')
    else:

        return render(request, 'creat-new.html')


def homepage(request):
    products = product.objects.all()
    return render(request, 'home page.html', {'products': products})


def orderform(request):
    if request.method == 'POST':
        name = request.user.username
        if cart.objects.filter(costumername=name).exists():
            name = request.POST.get('name')
            detail = request.POST.get('detail')
            price = request.POST.get('price')
            print(name)
            print(detail)
            print(price)
            cart.objects.filter(pk=3).update(productprice=price)
            
            return render(request, 'oder form.html')
        else:
            cart.objects.create(costumername=name, productname='null', productprice='0', productdetails='null')
            print(name, 'not exists')
            return render(request, 'oder form.html')
    else:
        return render(request, 'home page.html')


def orderplaced(request):
    return render(request, 'oredr placed.html')
