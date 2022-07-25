from . import views
from django.urls import path

urlpatterns = [
    path('', views.cartView, name='cartView'),
    path('addTocart/', views.addTocart, name='addTocart'),
    path('remove/<int:cid>', views.remove, name='remove'),
]