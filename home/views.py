from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .form import contactform
from .models import register, product, cart, order_list
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views.decorators.cache import cache_control


# from django.contrib.auth import logout

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
        return HttpResponse(render(request, 'login.html'))


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


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def homepage(request):
    if request.user.is_authenticated:
        products = product.objects.all()
        return render(request, 'home page.html', {'products': products})
    else:
        return redirect('/home')


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
            return render(request, 'oder form.html', {'details': t})
    else:
        return render(request, 'home page.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def shipping(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            names = request.user.username
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            cname = request.POST.get('cname')
            contry = request.POST.get('selection')
            street = request.POST.get('street')
            apartment = request.POST.get('apartment')
            city = request.POST.get('city')
            state = request.POST.get('state')
            postcode = request.POST.get('postcode')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            productname = request.POST.get('productname')
            productdetails = request.POST.get('productdetails')
            productimage = request.POST.get('productimage')
            productprice = request.POST.get('productprice')
            shipp = request.POST.get('shipp')
            order_list.objects.create(name=names, fname=fname, lname=lname, cname=cname, contry=contry, street=street,
                                      apartment=apartment, city=city, state=state, postcode=postcode, phone=phone,
                                      email=email, productname=productname, productdetails=productdetails,
                                      productprice=productprice, productimage=productimage, shipping_methode=shipp)
            return render(request, 'oredr placed.html', {'name': names})
    else:
        return redirect('/order-placed')


def cartpage(request):
    name = request.user.username
    t = cart.objects.filter(costumername=name)
    return render(request, 'cart page.html', {'products': t})


def orderplaced(request):
    return redirect('/order-placed')


def logouting(requset):
    if requset.method == 'POST':
        auth.logout(requset)
        return redirect("/home")
    else:
        return redirect("/home")
