from django.db import models


# Create your models here.
class register(models.Model):
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    objects = models.Manager()


class product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    Stock = models.IntegerField()
    image = models.CharField(max_length=5000)
    objects = models.Manager()
