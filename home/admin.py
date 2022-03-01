from django.contrib import admin
from .models import register, product


class registeradmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')


class productadmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'Stock', 'image')


# Register your models here.
admin.site.register(register, registeradmin)
admin.site.register(product, productadmin)
