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
    detail = models.CharField(max_length=1000, default='sume string')
    objects = models.Manager()

class cart(models.Model):
    costumername = models.CharField(max_length=50)
    productname = models.CharField(max_length=50)
    productprice = models.IntegerField()
    productdetails = models.CharField(max_length=1000)
    objects = models.Manager()


