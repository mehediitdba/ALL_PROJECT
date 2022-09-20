from curses.ascii import US
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def page_not_found(request):
    return HttpResponse("<h1>Page Not Found. go to /home_page </h1>")

def home_page(request):
    return render(request, 'hello_world.html')

#def home_page(request):
#    return HttpResponse("<h1>Hello World</h1>")

def about_page(request):
    return HttpResponse("<h1>About US</h1>")

def contact_page(request):
    return HttpResponse("<h1>Contact Us</h1>")

def page(request):
    return HttpResponse("<h1>page</h1>")