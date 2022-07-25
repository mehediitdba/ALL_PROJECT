from django.http import HttpResponse
from django.shortcuts import render
from .models import T_registration

# Create your views here.

# Create your views here.
def mPOSApp(request):
    return render(request, template_name='index.html')

def dashboard(request):
    return render(request, template_name='index.html')

def category_setup(request):
    return render(request, template_name='category_setup.html')

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
    return render(request, template_name='pages_contact.html')

def pages_register(request):
    return render(request, template_name='pages_register.html')


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
            print(fname, lname, email, phone,address,country,username,password)
            return render(request, 'pages_login.html', context={"login_successful" : True})
    return render(request, template_name='pages_register.html')

def pages_error_404(request):
    return render(request, template_name='pages_error_404.html')

def pages_blank(request):
    return render(request, template_name='pages_blank.html')