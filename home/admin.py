from django.contrib import admin
from .models import register


class registeradmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')


# Register your models here.
admin.site.register(register, registeradmin)
