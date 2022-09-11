from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.personal_form), #localhost:port:personal/list
    path('list/',views.personal_list),
]
