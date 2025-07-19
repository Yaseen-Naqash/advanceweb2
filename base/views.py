from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def myhomepage(request):
    phone = None
    username = 'myusernam'

    if request.method == 'POST':
        phone = request.POST.get('phone')

    context = {
            'phonekey' : phone,
            'usernamekey' : username,
        }
    
    return render(request,'home.html', context)

def login_page(request):
    return render( request , 'login.html')

def register_page(request):
    return render(request ,'register.html')

def products(request):
    return render(request, 'products.html')