from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from cartapp.models import CartItem
# Create your views here.
def home(request):
    if request.session.get('user'):
        cartCount=request.session['cartCount']
        return render(request, template_name='index.html', context={
            'cartCount':cartCount
        })

    return render(request, template_name='index.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            user = User.objects.create_user(
                first_name=fname, last_name=lname, username=username,
                email=email, password=password
            )
            user.save()
            return render(request, template_name='login.html')
        return render(request, template_name='register.html', context={
            'message': f"Password Confirmation is Wrong!"
        })
    return render(request, template_name='register.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            request.session['user'] = user.id
            request.session['cartCount'] = cartItems = CartItem.objects.filter(uid=user.id, ordered=False).count()
            return redirect('home')
        return render(request, template_name='login.html', context={
            'message': f"Inavalid Info!"
        })
    return render(request, template_name='login.html')

def Logout(request):
    logout(request=request)
    request.session['user'] = False
    request.session['cartCount'] = 0
    return redirect('home')


