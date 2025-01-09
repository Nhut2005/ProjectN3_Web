from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),  
    path('package', views.package, name="package"),
    path('package-edit/', views.edit_package, name="package-edit"),
]
