from webbrowser import get
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from requests import request, session
from .models import Order
from cartapp.models import CartItem
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

@method_decorator(login_required, name='dispatch')
class OrderView(TemplateView):
    #template_name = 'checkout.html'

   #@method_decorator(login_required)
    def get(self, request):

        cartItems = CartItem.objects.filter(uid=request.session.get('user'))
        total = sum([item.price for item in cartItems])
        context = {
            'cartitems': cartItems,
            'sub_total': total,
            'cartCount': request.session['cartCount']
        }
        return render(request, 'checkout.html', context=context)

    def post(self, request):
        print('In post')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        addr=request.POST.get('street_address')
        town=request.POST.get('city')
        zipcode=request.POST.get('zipCode')
        ph=request.POST.get('phone_number')
        comment=request.POST.get('comment')

        cartItems = CartItem.objects.filter(uid=request.session.get('user'), ordered=False)
        for item in cartItems:
            order=Order(
                cid=item,
                first_name=first_name,
                last_name=last_name,
                email=email,
                addr=addr,
                town=town,
                zipcode=zipcode,
                ph=ph,
                comment=comment,
                status='Pending'
            )
            order.save()
            item.ordered=True
            item.save()
            request.session['cartCount'] -= 1
        
        context = {
            'cartCount': request.session['cartCount']
        }
        return redirect('home')