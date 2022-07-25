from django.http import HttpResponse
from django.shortcuts import render
from .models import User
#from django.contrib.auth.models import User
# Create your views here.


def hello(request):
    return HttpResponse("Hello Python")


def signup(request):
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordc = request.POST.get('passwordc')
        if password != passwordc:
            return render(request, 'signup.html', context={"password_notmatch" : True})
        if password == passwordc:
            user = User(
                username=username,
                email=email,
                password=password
            )
            user.save()
        print(username, email, password, passwordc)
        return render(request, 'login.html', context={"login_successful" : True})
    return render(request, 'login.html')

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')
        user=User.objects.get(username=username, password=password)
        if user and password == user.password:
            return render(request, 'home.html', context={
                'user':user
            })
        return render(request, 'signup.html')
    return render(request, 'login.html')

def email(request):
    return render(request, 'email.html')

def emailsend(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        subject = request.POST.get('subject')
        messagebody = request.POST.get('messagebody')
        if email is not None and username is not None and subject is not None and messagebody is not None: 
                email = Email(
                username=username,
                email=email,
                subject=subject,
                messagebody=messagebody
            )
                email.save()
