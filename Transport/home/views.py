from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Order
from .models import Customer
from .models import Employee



# Create your views here.

def home (request):
    return render(request, 'home/home.html')

def package(request):
    package = Order.objects.all()  
    template = loader.get_template('home/package/package.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def edit_package(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/package/package-edit.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def employee(request):
    employee = Employee.objects.all()  
    template = loader.get_template('home/employee/employee.html')
    context = {
        'employee': employee,
    }
    return HttpResponse(template.render(context, request))

def edit_employee(request):
    employee = Employee.objects.filter(id=1).first() 
    template = loader.get_template('home/employee/employee-edit.html')
    context = {
        'employee': employee,
    }
    return HttpResponse(template.render(context, request))

def customer(request):
    customer = Customer.objects.all()  
    template = loader.get_template('home/customer/customer.html')
    context = {
        'customer': customer,
    }
    return HttpResponse(template.render(context, request))

def edit_customer(request):
    employee = Customer.objects.filter(id=1).first() 
    template = loader.get_template('home/customer/customer-edit.html')
    context = {
        'customer': customer,
    }
    return HttpResponse(template.render(context, request))

