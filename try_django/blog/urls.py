from django.urls import path, include, re_path #url
from . import views

urlpatterns = [
        path('', views.blog_post_detail_page, name='blog_post_detail_page'),
        ]