from ast import keyword
from curses import keyname
from unicodedata import category
from django.shortcuts import render
from .models import Product


# Create your views here.
def trending(request):
    items = Product.objects.all()
    cats = sorted({item.category for item in items})
    return render(request=request, template_name='trending.html', context={
        'items': items,
        'cats': cats,
        'cartCount':request.session['cartCount']
    })


def details(request, pid):
    item = Product.objects.get(pid=pid)
    return render(request=request, template_name='product-details.html', context={
        'item': item,
        'cartCount':request.session['cartCount']
    })


def filterByCat(request, cat):
    items = Product.objects.filter(category=cat)
    cats = [cat, ]
    return render(request=request, template_name='trending.html', context={
        'items': items,
        'cats': cats,
        'cartCount':request.session['cartCount']
    })


def search(request):
    keywords = request.POST.get('keywords').split(' ')
    items = Product.objects.filter(title__icontains=keywords[0])
    items = items.union(Product.objects.filter(
        description__icontains=keywords[0]))
    for keyword in keywords[1:]:
        items = items.union(Product.objects.filter(title__icontains=keyword))
        items = items.union(Product.objects.filter(
            description__icontains=keyword))
    cats = sorted({item.category for item in items})
    return render(
        request=request, template_name='search_results.html', context={
            'items': items, 
            'cats': cats, 
            'cartCount':request.session['cartCount']
        }
    )
