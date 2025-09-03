from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person, Blog
from django.contrib import messages


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):

    blogs = Blog.objects.all()
    # users = Person.objects.all()
    # for user in users:
    #     user.set_password(user.password)
    #     user.save()

    context = {
        'blogs':blogs,
    }
    
    return render(request,'home.html', context)

def login_page(request):
    if request.method == 'POST':

        myusername = request.POST.get('username')
        mypassword = request.POST.get('password')
        user = authenticate(username=myusername,password=mypassword)
        if user is not None:

            login(request, user)
            messages.success(request,'your logged in successfully')

            return redirect('my_home_url')
        else:
            messages.error(request,'username or password is wrong!')
            return redirect('my_login_url')
    return render( request , 'login.html')


def logout_command(request):
    logout(request)
    messages.success(request,'your logged out successfully!')

    return redirect('my_login_url')


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
        user.set_password(password1)
        user.save()
        messages.success(request, 'user created')
        return redirect('my_login_url')
        # user.save()
        

        pass

# messages.info(request, "Three credits remain in your account.")
# messages.success(request, "Profile details updated.")
# messages.warning(request, "Your account expires in three days.")
# messages.error(request, "Document deleted.")

    return render(request ,'register.html')

def details(request,pk):


    blog = Blog.objects.get(id=pk)
    context = {
        'blog':blog,
    }
    return render(request, 'details.html', context)

def create_blog(request):
    if not request.user.is_authenticated:
        return HttpResponse('403')
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        author = request.POST.get('author')
        image = request.FILES.get('image')

        user = Person.objects.get(id=author)

        blog = Blog.objects.create(
            title=title,
            body=body,
            author=user,
            image=image,
        )
        messages.success(request, 'blog created')

        return redirect('my_home_url')
    

    users = Person.objects.all()
    context = {'users':users}
    return render(request, 'create.html', context)


def update_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    users = Person.objects.all()
    if not request.user == blog.author:
        return HttpResponse('403')
    context = {
        'blog':blog,
        'users':users,
    }

    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        author = request.POST.get('author')
        image = request.FILES.get('image')
        
        user = Person.objects.get(id=author)
        blog = Blog.objects.get(id=pk)
        print(author)
        blog.title=title
        blog.body=body
        blog.author=user
        if image:
            blog.image=image

        blog.save()
        

        messages.success(request, 'blog updated')

        return redirect('my_home_url')



    return render(request, 'update.html', context)

def delete_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    if not request.user == blog.author:
        return HttpResponse('403')
    blog.delete()
    messages.success(request, 'blog deleted')
    return redirect('my_home_url')