from django.db.models import ObjectDoesNotExist
from django.contrib.auth.decorators import *
from django.contrib.auth.forms import User
from django.contrib import messages
from django.contrib.auth import *
from django.shortcuts import *
from django.urls import reverse
from accounts.forms import *
import re

def login_view(request):
    if request.method == 'POST':
        loginInfo = request.POST.get('loginInfo')
        password = request.POST.get('password')
        if not loginInfo or not password:
            print("Please provide both login info and password.")
            messages.error(request, 'Please provide both login info and password.')
            return render(request, "accounts/login.html", {'message': 'Please provide both login info and password.'})
        emailPattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(emailPattern, loginInfo):
            try:
                userFinder = User.objects.get(email=loginInfo)
            except ObjectDoesNotExist:
                print("Invalid email. User does not exist.")
            else:
                user = authenticate(request, username=userFinder.username, password=password) # Authenticates the user with the email and password provided (Checking if such user exists)
                if user is not None:
                    login(request, user)
                    print(user)
                    return redirect('/')
                else:
                    print("Incorrect password")
        else:
            user = authenticate(request, username=loginInfo, password=password)
            if user is not None:
                login(request, user)
                print(user)
                return redirect('/')
            else:
                print("Incorrect password")
    else:
        message = ""
        return render(request, "accounts/login.html", {'message': message})

@login_required # A decorator to determine that a function can only be executed when a user has logged in before
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('/')

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password or len(password) < 8:
            message = messages.error(request, 'Passwords do not match (or password is less than 8 characters)')
            return redirect('accounts_app:signup', context={'message': message})
        else:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                # message = messages.error(request, 'User already exists')
                # return reverse('accounts_app:login', context={'message': message})
                return redirect('/')
            else:
                new_user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                )
                new_user.save()
                login(request, new_user)
                return redirect('/')
    else:
        return render(request, "accounts/signup.html")