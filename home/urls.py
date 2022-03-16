from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='login.html'),
    path('creat-new', views.creat, name='creat-new.html'),
    path('home-page', views.homepage, name='home page.html'),
    path('order-form', views.orderform, name='oder form.html'),
    path('order-placed', views.orderplaced, name='oredr placed.html'),
    path('shipping', views.shipping, name='oder form'),
    path('logouting', views.logouting, name='login.html'),
    path('cart', views.cartpage, name= "cart page.html")
]
