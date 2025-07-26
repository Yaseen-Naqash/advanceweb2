from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
# Create your views here.

def myhomepage(request):
    phone = None
    username = 'yasin'
    mylist = ['apple', 'bannana', 'orange', 'lemon', 'cherry']
    if request.method == 'POST':
        phone = request.POST.get('phone')




    context = {
            'phonekey' : phone,
            'usernamekey' : username,
            'mylist':mylist,
        }
    
    return render(request,'home.html', context)

def login_page(request):
    return render( request , 'login.html')

def register_page(request):
    return render(request ,'register.html')

def products(request):
    return render(request, 'products.html')