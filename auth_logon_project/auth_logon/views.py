from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("Login Success"))
            return render(request,'authenticate/home.html', {})
        else:
            messages.warning(request,("There Was An Error Login In, Try Agin..."))
            return redirect('/login/login_user')

    else:
        return render(request,'authenticate/login.html', {})
