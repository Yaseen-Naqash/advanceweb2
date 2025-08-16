from django.contrib import admin
from django.urls import path
from .views import home, login_page, register_page, details, logout_command

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',home, name='my_home_url'),
    path('login/',login_page, name='my_login_url'),
    path('logout/',logout_command , name='my_logout_url'),

    path('register/',register_page, name='my_register_url'),
    path('products/',details, name='my_details_url'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)