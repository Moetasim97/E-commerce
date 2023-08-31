from django.db import models
from .validators import validate_password
from django.contrib.auth import User
# Create your models here.




class Customer(User):
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=15,help_text='Enter a valid Mobile Number: ')

class Admin(User):
    jobtitle=models.CharField
    hiredate=models.DateField(auto_now=True)




# class Order(models.Model):
#     createDate = models.DateField(auto_now=True)
    