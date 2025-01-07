from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),  
    path('employee', views.employee, name="employee"),
    path('edit-employee', views.edit_employee, name="edit-employee"),
]
