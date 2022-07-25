from itertools import product
from multiprocessing import context
import django
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import CartItem
from django.contrib.auth.models import User
from productApp.models import Product

# Create your views here.


@login_required
def cartView(request):
    uid = request.session.get('user')
    cartItems = CartItem.objects.filter(uid=uid, ordered=False)
    total = sum([item.price for item in cartItems])
    context = {
        'cartitems': cartItems,
        'sub_total': total,
        'cartCount': request.session['cartCount']
    }
    return render(request=request, template_name='cart.html', context=context)


@login_required
def addTocart(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        pid = request.POST.get('pid')
        qty = request.POST.get('quantity')
        print(qty, uid, pid)
        user = User.objects.get(id=uid)
        product = Product.objects.get(pid=pid)
        cartItem = CartItem(
            uid=user,
            pid=product,
            qty=qty,
            price=(float(qty) * float(product.price))
        )
        cartItem.save()
        request.session['cartCount'] += 1
        return redirect('cartView')
    return redirect('home')


@login_required
def remove(request, cid):
    CartItem.objects.get(cid=cid).delete()
    request.session['cartCount'] -= 1
    return redirect('cartView')
