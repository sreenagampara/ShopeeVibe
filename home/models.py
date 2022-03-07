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
    productprice = models.FloatField()
    productdetails = models.CharField(max_length=1000)
    productimage = models.CharField(max_length=5000, default='some string')
    objects = models.Manager()


class order_list(models.Model):
    name = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50, default='Not Available')
    cname = models.CharField(max_length=50, default='Not Available')
    contry = models.CharField(max_length=50)
    street = models.CharField(max_length=500)
    apartment = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default='Not Available')
    productname = models.CharField(max_length=50, default='Not Available')
    productprice = models.FloatField(default=0)
    productimage = models.CharField(max_length=5000, default='Not Available')
    shipping_methode = models.CharField(max_length=50, default='Not Available')
    productdetails = models.CharField(max_length=500, default='Not available')
    objects = models.Manager()
