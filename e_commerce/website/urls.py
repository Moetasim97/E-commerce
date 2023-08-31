from . import views
from django.urls import path

urlpatterns= [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('thanks',views.thanks,name="thanks"),
    path('login',views.login,name='login')
]
