from . import views
from django.urls import path
from django.contrib.auth import views as auth_views




urlpatterns= [
    path('',views.home,name="home"),
    path('register',views.registerCust,name="registerCustomer"),
    path('registerAdmin',views.registerAdmin,name='registerAdmin'),
    path('thanks',views.thanks,name="thanks"),
    path('login',views.loginView,name='login'),
    path('checkout',views.shoppingCart,name='shoppingCart'),
    path('men',views.renderMen,name='men'),
    path('kids',views.renderKids,name='kids'),
    path('women',views.renderWomen,name='women'),
    path('confirmation',views.orderConfirmView,name='orderConfirmation'),
    path('logout/', auth_views.LogoutView.as_view(next_page='http://127.0.0.1:8000'), name='logout'),
]
