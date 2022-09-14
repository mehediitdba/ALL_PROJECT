from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.personal_form, name='personal_insert'), #get and post req. for  for insert operation    #localhost:port:personal/list
    path('<int:id>/', views.personal_form, name='personal_update'), #get and post req. for update operation
    path('delete/<int:id>/',views.personal_delete,name='personal_delete'),
    path('list/',views.personal_list,name='personal_list'), #get req. to retrieve and display all record
]
