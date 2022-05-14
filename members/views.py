from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#import Users
from django.contrib.auth.models import User

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('Error logging in - please try again!'))
            return redirect('login')
    else:
        return render(request, 'authentication/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out!'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            print(username, email, password)
            if User.objects.filter(username=username).exists():
                messages.success(request, ('That username is taken - please try another!'))
                print('That username is taken - please try another!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.success(request, ('That email is being used - please try another!'))
                    print('That email is being used - please try another!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    messages.success(request, ('You are now registered and can log in!'))
                    print('You are now registered and can log in!')
                    return redirect('login')
        else:
            print('passwords do not match')
            messages.success(request, ('Passwords do not match - please try again!'))
            return redirect('register')
    else:
        return render(request, 'authentication/register.html')