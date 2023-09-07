from django.db import models
from .validators import validate_password
from django.contrib.auth.models import User
# Create your models here.






class CustomAdmin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    jobtitle = models.CharField(max_length=100,null=True)
    
  
    
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=300,null=True)
    phone = models.CharField(max_length=15,help_text='Enter a valid Mobile Number: ', null=True)

    def __str__(self):
        return self.user.username



class Product(models.Model):
    nameEn=models.CharField(max_length=100)
    nameAr=models.CharField(max_length=100)
    unitPrice=models.DecimalField(max_digits=6,decimal_places=2)
    stockQuantity=models.IntegerField()
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    details=models.ManyToManyField('Product',through='OrderDetails')
    

    def __str__(self):
        return self.nameEn

class ProductImages(models.Model):
    image=models.ImageField()
    product=models.ForeignKey('Product',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.image)
    

class Category(models.Model):
    name=models.CharField(max_length=100)



    def __str__(self):
        return self.name
    
# Those are the choices that are going to be represented in the admin interface for determining order status.
OPTIONS=(('First Option','Pending'),
         ('Second Option','Approved'),
         ('Third Option','Declined'),
         ('Fourth Option','Shipped'),
         ('Fifth Option','Delivered'))

class Order(models.Model):
    creationDate = models.DateField(auto_now=True)
    status=models.CharField(max_length=100,choices=OPTIONS)
    details=models.ManyToManyField('Product',through='OrderDetails')
    totalPrice=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE)

class OrderDetails(models.Model):
    product=models.ForeignKey('Product',on_delete=models.CASCADE)
    order=models.ForeignKey('Order',on_delete=models.CASCADE)
    orderedCount=models.IntegerField(null=True,blank=True)
    
    
    



    

    