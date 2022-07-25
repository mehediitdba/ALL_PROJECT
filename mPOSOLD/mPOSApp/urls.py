from . import views
from django.urls import path

urlpatterns = [
    path('', views.mPOSApp, name='mPOSApp'),
    path('dashboard', views.dashboard, name='dashboard'),

    path('category_setup', views.category_setup, name='category_setup'),
    path('item_setup', views.item_setup, name='item_setup'),
    path('daily_invoice', views.daily_invoice, name='daily_invoice'),
    path('order_entry', views.order_entry, name='order_entry'),
    path('item_cancel', views.item_cancel, name='item_cancel'),
    path('invoice_cancel', views.invoice_cancel, name='invoice_cancel'),
    path('sales_report', views.sales_report, name='sales_report'),
    path('collection_report', views.collection_report, name='collection_report'),
    path('due_report', views.due_report, name='due_report'),
    path('purchase_order', views.purchase_order, name='purchase_order'),
    path('purchase_receive', views.purchase_receive, name='purchase_receive'),
    path('item_stock', views.item_stock, name='item_stock'),

    path('users_profile', views.users_profile, name='users_profile'),

    path('pages_faq', views.pages_faq, name='pages_faq'),
    path('pages_contact', views.pages_contact, name='pages_contact'),
    path('pages_register', views.pages_register, name='pages_register'),
    path('pages_login', views.pages_login, name='pages_login'),
    path('pages_error_404', views.pages_error_404, name='pages_error_404'),
    path('pages_blank', views.pages_blank, name='pages_blank'),


]