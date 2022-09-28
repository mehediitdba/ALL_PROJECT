from django.urls import path, include, re_path #url
from . import views

urlpatterns = [
        path('', views.page_not_found, name='page_not_found'),
		path('home_page/', views.home_page, name='home_page'), 
        path('home_page2/', views.home_page2, name='home_page2'),
        path('about/', views.about_page, name='about_page'),
        #path('contact/', views.contact_page, name='contact_page'),
        re_path(r'^contacts?/$', views.contact_page, name='contact_page'),
        #path('page/', views.page, name='page'),
        #path('pages/', views.page, name='page'),
        re_path(r'^pages?/$', views.page, name='page'),

        ]