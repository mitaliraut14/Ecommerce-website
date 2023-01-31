from django.db import models

# Create your models here.
class Product(models.Model):

    pname=models.CharField(max_length=100,null=True)
    image=models.ImageField(null=True)
    shape=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    price=models.IntegerField()

class User(models.Model):

    username=models.CharField(max_length=100,)
    password=models.CharField(max_length=100, null = True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=100)

class Recommendation(models.Model):

    product_ID=models.ForeignKey(Product, on_delete=models.CASCADE)
    user_ID=models.ForeignKey(User, on_delete=models.CASCADE)