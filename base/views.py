from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person, Blog
from django.contrib import messages

# Create your views here.

def myhomepage(request):
    # Person.objects.get() ✅
    # Person.objects.filter() ✅
    # Person.objects.all() ✅
    # Person.objects.get_or_create() ✅
    # Person.objects.create() ✅

    phone = None
    myPerson = None
    username = 'yasin'
    mylist = ['apple', 'bannana', 'orange', 'lemon', 'cherry']
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        if Person.objects.filter(phone=phone,password=password).exists():
            myPerson = Person.objects.get(phone=phone,password=password)
            # myPerson.delete()
            # myPerson.password = '258456'
            # myPerson.save()


    




    context = {
            'phonekey' : phone,
            'usernamekey' : username,
            'mylist':mylist,
            'person':myPerson,
            'users':allofUsers,
        }
    
    return render(request,'home.html', context)

def login_page(request):
    return render( request , 'login.html')

def register_page(request):

    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password')
        password2 = request.POST.get('repeatedPassword')
        email = request.POST.get('email') if request.POST.get('email') else ''

        if password1 != password2:
            messages.error(request, "password does not match")
            return redirect('my_register_url')





        user = Person.objects.create(
            first_name = firstName,
            last_name = lastName,
            phone = phone,
            password = password1,
            email = email,
            is_stuff = False,
            
        )
        messages.success(request, 'user created')
        return redirect('my_login_url')
        # user.save()
        

        pass

# messages.info(request, "Three credits remain in your account.")
# messages.success(request, "Profile details updated.")
# messages.warning(request, "Your account expires in three days.")
# messages.error(request, "Document deleted.")

    return render(request ,'register.html')

def products(request):
    return render(request, 'products.html')