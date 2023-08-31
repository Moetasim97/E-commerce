from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # isActive = models.BooleanField()
    # email = models.EmailField()
    # fullName = models.CharField()

    class Meta:
        abstract = True

class Customer(User):
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=15,help_text='Enter a valid Mobile Number: ')


# class Order(models.Model):
#     createDate = models.DateField(auto_now=True)
    