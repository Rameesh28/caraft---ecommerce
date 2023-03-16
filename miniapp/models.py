from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class usermodel(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.username

class shopmodel(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username


class productmodel(models.Model):
    pname=models.CharField(max_length=30)
    pid=models.CharField(max_length=10)
    price=models.IntegerField()
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to='miniapp/static')
    def __str__(self):
        return self.pname


class cartmodel(models.Model):
    cartname=models.CharField(max_length=30)
    pid=models.CharField(max_length=10)
    cid=models.CharField(max_length=6)
    cartprice=models.IntegerField()
    cartdescription=models.CharField(max_length=100)
    cartimage=models.ImageField(upload_to='miniapp/static')
    def __str__(self):
        return self.cartname


class productdisplaymodel(models.Model):
    productname=models.CharField(max_length=30)
    pid=models.CharField(max_length=10)
    price=models.IntegerField()
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to='miniapp/static')
    def __str__(self):
        return self.name