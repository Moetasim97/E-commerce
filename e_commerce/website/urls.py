from . import views
from django.urls import path

urlpatterns= [
    path('',views.home,name="home"),
    path('register',views.registerCust,name="registerCustomer"),
    path('registerAdmin',views.registerAdmin,name='registerAdmin'),
    path('thanks',views.thanks,name="thanks"),
    path('login',views.login,name='login'),
    path('checkout',views.shoppingCart,name='shoppingCart'),
    path('men',views.renderMen,name='men'),
    path('kids',views.renderKids,name='kids'),
    path('women',views.renderWomen,name='women')
]
