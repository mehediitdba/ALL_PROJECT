from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import PersonalForm
from .models import Personal

# Create your views here.
def personal_list(request):
    context={'personal_list':Personal.objects.all()}
    return render(request, "personal_reg/personal_list.html",context)

def personal_form(request,id=0):
    if request.method=="GET":
        if id==0:
            form = PersonalForm()
        else:
            personal=Personal.objects.get(pk=id)
            form = PersonalForm(instance=personal)
        return render(request, "personal_reg/personal_form.html",{'form':form})
    else:
        if id == 0:
            form = PersonalForm(request.POST)
        else:
            personal=Personal.objects.get(pk=id)
            form=PersonalForm(request.POST,instance=personal)
        if form.is_valid():
            form.save()
        return redirect('/personal/list')

def personal_delete(request,id):
    personal=Personal.objects.get(pk=id)
    personal.delete()
    return redirect('/personal/list')