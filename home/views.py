from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import Contact
from home.models import Blog
from django.contrib import messages
import math


# Create your views here.

# def home(request):
#     return render(request,'index.htm' )

def home(request):
    # return HttpResponse("THIS IS FIRST WEB ON DJANGO")
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
       # print(name , email , desc)
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()
    return render(request, 'contact.html')


def search(request):
    # allposts = Blog.objects.all()

    query = request.GET['query']
    if len(query) > 70 and len(query) < 0:
        allposts = []
    else:
        # q1 = Blog.objects.filter(title__icontains=query)
        # q2 = Blog.objects.filter(content__icontains=query)
        # allposts = q1.union(q2)
        allposts = Blog.objects.filter(title__icontains=query)

    params = {'allposts': allposts}
    return render(request, 'search.html',  params)

# Sign Up Handling


def signup(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Checking Error input
        if len(username) > 15:
            messages.error(request, 'Username must be under 15 Char')
            return redirect('/')

        if not username.isalnum():
            messages.error(request, 'Username must not container special char')
            return redirect('/')

        if pass1 != pass2:
            messages.error(request, 'Password does not match')
            return redirect('/')

        ######
        users = User.objects.create_user(username, email, pass1)
        users.first_name = f_name
        users.last_name = l_name
        users.save()
        messages.success(request, 'Acount Create Succesfully')
        return redirect('/')

    else:
        return HttpResponse('Error 404')


# Login
def login(request):
    if request.method == 'POST':
        loginuser = request.POST['loginuser']
        password = request.POST['password']
        user = authenticate(username=loginuser, password=password)

        if user is not None:
            login(request)
            messages.success(request, "Login Successfully")
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/')


# Logout
def logout(request):
    pass
