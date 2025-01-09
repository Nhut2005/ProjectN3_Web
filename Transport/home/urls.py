from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),  
    path('package', views.package, name="package"),
    path('package-edit/', views.edit_package, name="package-edit"),

    path('employee', views.employee, name="employee"),
    path('employee-edit/', views.edit_employee, name="employee-edit"),

    path('customer', views.customer, name="customer"),
    path('customer-edit/', views.edit_customer, name="customer-edit"),
]
