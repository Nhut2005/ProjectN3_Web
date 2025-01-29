from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),  
    path('package/', views.package, name="package"),
    path('package-edit/', views.edit_package, name="package-edit"),
    path('package-delete/', views.delete_package, name="package-delete"),
    path('package-new/', views.new_package, name="package-new"),
    path('package-search/', views.search_packages, name="package-search"),

    path('employee', views.employee, name="employee"),
    path('employee-edit/', views.edit_employee, name="employee-edit"),
    path('employee-delete/', views.delete_employee, name="employee-delete"),
    path('employee-new/', views.new_employee, name="employee-new"),

    path('customer', views.customer, name="customer"),
    path('customer-edit/', views.edit_customer, name="customer-edit"),
    path('customer-delete/', views.delete_customer, name="customer-delete"),
    path('customer-new/', views.new_customer, name="customer-new"),
]
