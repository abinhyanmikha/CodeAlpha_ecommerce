from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def Register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']


        if password!= confirm_password:
            messages.error(request,'password doesnt match')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request,'username already registered')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request,'email already registered')
            return redirect('register')

        user=User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        messages.success(request,'user registered successfully')
        return redirect('login')

    return render(request,'accounts/register.html')

def  Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'accounts/login.html')


def Logout(request):
    logout(request)
    return redirect('login')
