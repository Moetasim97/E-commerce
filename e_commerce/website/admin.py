from django.contrib import admin
from .models import Customer,CustomAdmin,Product,ProductImages,Category,Order,OrderDetails
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
# Register your models here.
admin.site.register(Customer)
admin.site.register(CustomAdmin)
admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderDetails)



