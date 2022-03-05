from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .form import contactform
from .models import register, product, cart
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views.decorators.cache import never_cache


# from django.contrib.auth import logout

# Create your views here.
@never_cache
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
    m = "This User name alredy tacken try another"
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            return render(request, 'creat-new.html', {'message': m})
        else:
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
        detail = request.POST.get('detail')
        price = request.POST.get('price')
        product_name = request.POST.get('name')
        image = request.POST.get('image')
        t = cart.objects.filter(costumername=name)
        if cart.objects.filter(costumername=name).exists():

            for item in t:
                item.productname = product_name
                item.productprice = price
                item.productdetails = detail
                item.productimage = image
                item.save()

            return render(request, 'oder form.html', {'t': t})
        else:
            cart.objects.create(costumername=name, productname=product_name, productprice=price, productdetails=detail)
            print(name, 'not exists')
            return render(request, 'oder form.html', {'details': t})
    else:
        return render(request, 'home page.html')


def shipping(request):
    names = request.user.username
    name = request.POST.get('fname')
    print(names)
    print(name)
    return render(request, 'oredr placed.html', {'name': names})


def orderplaced(request):
    return render(request, 'oredr placed.html')


@never_cache
def logouting(requset, back_page=None):
    if requset.method == 'POST':
        auth.logout(requset)
        return HttpResponseRedirect("/home")
    return render(requset, 'home page.html')
