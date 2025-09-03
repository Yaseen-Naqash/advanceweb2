from django.contrib import admin
from django.urls import path
from .views import home, login_page, update_blog, delete_blog, register_page, create_blog, details, logout_command

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',home, name='my_home_url'),
    path('login/',login_page, name='my_login_url'),
    path('logout/',logout_command , name='my_logout_url'),
    path('register/',register_page, name='my_register_url'),
    
    path('details/<int:pk>/',details, name='my_details_url'),
    path('create/',create_blog, name='my_create_url'),
    path('update/<int:pk>/',update_blog, name='my_update_url'),
    path('delete/<int:pk>/',delete_blog, name='my_delete_url'),


]


