from django.contrib import admin
from django.urls import path
from .views import myhomepage, login_page, register_page, products

urlpatterns = [
    path('',myhomepage, name='my_home_url'),
    path('login/',login_page, name='my_login_url'),
    path('register/',register_page, name='my_register_url'),
    path('products/',products, name='my_products_url'),
]
