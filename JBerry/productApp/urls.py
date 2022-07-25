from . import views
from django.urls import path

urlpatterns = [
    path('trending/', views.trending, name='trending'),
    path('details/<int:pid>/', views.details, name='details'),
    path('filterByCat/<cat>/', views.filterByCat, name='filterByCat'),
    path('search/', views.search, name='search'),
]