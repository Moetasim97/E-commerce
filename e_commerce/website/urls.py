from . import views
from django.urls import path

urlpatterns= [
    path('',views.home,name="home"),
    path('register',views.registerCust,name="registerCustomer"),
    path('registerAdmin',views.registerAdmin,name='registerAdmin'),
    path('thanks',views.thanks,name="thanks"),
    path('login',views.login,name='login')
]
