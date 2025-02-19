from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),  
    

    path('package/', views.package, name="package"),
    path('create-package', views.create_package, name="create_package"),
    path('package-delete/', views.delete_package, name="package-delete"),
    path('package-new/', views.new_package, name="package-new"),
    

    path('employee', views.employee, name="employee"),
    path('employee-edit/', views.edit_employee, name="employee-edit"),
    path('employee-delete/', views.delete_employee, name="employee-delete"),
    path('employee-new/', views.new_employee, name="employee-new"),

    path('customer', views.customer, name="customer"),
    path('customer-edit/', views.edit_customer, name="customer-edit"),
    path('customer-delete/', views.delete_customer, name="customer-delete"),
    path('customer-new/', views.new_customer, name="customer-new"),

    path('login/', views.login_user, name='login_user'),
    path('register/', views.register_user, name='register_user'),
    path("account", views.view_account, name="account"),
    path('login/', views.login_user, name='login_user'),

    path('my-order/', views.my_order, name='my_order'),
    path('addresses/', views.my_addresses, name='addressess'),
    path('voucher/', views.my_voucher, name='voucher'),
    path('setting/', views.my_setting, name='setting'),

    path('blog/', views.my_blog, name='blog'),
    path('question/', views.my_question, name='question'),
    path('contact/', views.my_contact, name='contact'),

    path('manager/', views.view_manager, name='manager'),
    path('shipping-menu/', views.view_shipmenu, name='shipping-menu'),
    path('shipping-process/', views.view_shipprocess, name='shipping-process'),
    path('price-list/', views.view_pricelist, name='price-list'),
    path('dashboard-report', views.view_dashboard, name='dashboard-report'),
    path('feedback', views.view_feedback, name='feedback'),
    path('customer-profile', views.view_profile, name='customer-profile'),

    path('dich-vu-van-chuyen-ca-koi-nhat', views.view_dichvu, name='vanchuyenca'),
    path('profile', views.view_tkprofile, name='profile'),
    path('bang-gia', views.price_list, name='bang-gia'),
    path('koi-transport', views.view_congty, name='cong-ty'),
 

]
