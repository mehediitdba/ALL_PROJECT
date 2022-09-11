from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import PersonalForm

# Create your views here.
def personal_list(request):
    return render(request, "personal_reg/personal_list.html")

def personal_form(request):
    form = PersonalForm()
    return render(request, "personal_reg/personal_form.html",{'form':form})

def personal_delete(request):
    return