from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import T_category, T_registration, T_messages
from django.contrib import messages
from sequences import get_next_value

# Create your views here.

# Create your views here.
def mPOSAppv2(request):
    return render(request, template_name='index_main.html')

def m_services(request):
    return render(request, template_name='services_main.html')


def m_about(request):
    return render(request, template_name='about_main.html')


def m_contact(request):
    return render(request, template_name='contact_main.html')

def dashboard(request):
    return render(request, template_name='index.html')

def category_setup(request):
    if request.method == 'POST':
        catactive = request.POST.get('catactive')
        catid = request.POST.get('catid')
        catname=request.POST.get('catname')
        if catid is not None:
            t_category = T_category(
                catactive=catactive,
                catid=catid,
                catname=catname
            )
            t_category.save()
            messages.success(request, 'Data Save Successfully')
            return render(request, template_name='category_setup.html')
    return render(request, template_name='category_setup.html')

def category_setup_v(request):
    from django.core import serializers
    category = serializers.serialize("python", T_category.objects.all())

    context={
        'category':category,
    }
    return render(request, 'category_setup.html', context)

def item_setup(request):
    return render(request, template_name='item_setup.html')

def daily_invoice(request):
    return render(request, template_name='daily_invoice.html')

def order_entry(request):
    return render(request, template_name='order_entry.html')

def item_cancel(request):
    return render(request, template_name='item_cancel.html')

def invoice_cancel(request):
    return render(request, template_name='invoice_cancel.html')

#
def sales_report(request):
    return render(request, template_name='sales_report.html')

def collection_report(request):
    return render(request, template_name='collection_report.html')    

def due_report(request):
    return render(request, template_name='due_report.html')

def purchase_order(request):
    return render(request, template_name='purchase_order.html')

def purchase_receive(request):
    return render(request, template_name='purchase_receive.html')

def item_stock(request):
    return render(request, template_name='item_stock.html')
#    

def users_profile(request):
    return render(request, template_name='users_profile.html')

def pages_faq(request):
    return render(request, template_name='pages_faq.html')

def pages_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject= request.POST.get('subject')
        message = request.POST.get('message')
        t_messages = T_messages(
            id=get_next_value(),
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        t_messages.save()
        messages.success(request, 'Data Save Successfully')
        return render(request, template_name='pages_contact.html')
    return render(request, template_name='pages_contact.html')




def pages_login(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        country = request.POST.get('country')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password != cpassword:
            return render(request, pages_register.html, context={"password_notmatch":True})
        if password == cpassword:
            t_registration = T_registration(
                fname=fname,
                lname=lname,
                email=email,
                phone=phone,
                address=address,
                country=country,
                username=username,
                password=password
            )
            t_registration.save()
            messages.success(request, 'Data Save Successfully')
            print(fname, lname, email, phone,address,country,username,password)
            return render(request, 'pages_login.html', context={"login_successful" : True})
    return render(request, template_name='pages_login.html')


def pages_register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')  
        user = authenticate(username=username, password=password)  
        if user is not None:
            login(request=request, user=user)
            messages.success(request, 'Successfully Login')
            return render(request, 'index.html', context={"reg_successful" : True})
        else:
            messages.success(request, 'UnSuccessfully Login')
            return render(request, 'pages_login.html', context={"reg_successful" : False})
    return render(request, template_name='pages_register.html')
    
def pages_error_404(request):
    return render(request, template_name='pages_error_404.html')

def pages_blank(request):
    return render(request, template_name='pages_blank.html')

