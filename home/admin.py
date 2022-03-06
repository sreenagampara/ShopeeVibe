from django.contrib import admin
from .models import register, product, cart, order_list


class registeradmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')


class productadmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'Stock', 'image', 'detail')


class cartadmin(admin.ModelAdmin):
    list_display = ('costumername', 'productname')


class order_listadmin(admin.ModelAdmin):
    list_display = ('name', 'productname', 'shipping_methode')


# Register your models here.
admin.site.register(register, registeradmin)
admin.site.register(product, productadmin)
admin.site.register(cart, cartadmin)
admin.site, register(order_list, order_listadmin)
