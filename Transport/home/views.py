from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Order
from .models import Customer
from .models import Employee



# Create your views here.

def home (request):
    return render(request, 'home/home.html')
#package
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

def delete_package(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/package/package-delete.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def new_package(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/package/package-new.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))
#employee
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

def delete_employee(request):
    employee = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/employee/employee-delete.html')
    context = {
        'employee': employee,
    }
    return HttpResponse(template.render(context, request))

def new_employee(request):
    package = Order.objects.filter(id=1).first() 
    employee = loader.get_template('home/employee/employee-new.html')
    context = {
        'employee': employee,
    }
    return HttpResponse(template.render(context, request))
#customer
def customer(request):
    customer = Customer.objects.all()  
    template = loader.get_template('home/customer/customer.html')
    context = {
        'customer': customer,
    }
    return HttpResponse(template.render(context, request))

def edit_customer(request):
    customer = Customer.objects.filter(id=1).first() 
    template = loader.get_template('home/customer/customer-edit.html')
    context = {
        'customer': customer,
    }
    return HttpResponse(template.render(context, request))

def delete_customer(request):
    customer = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/customer/customer-delete.html')
    context = {
        'customer': customer,
    }
    return HttpResponse(template.render(context, request))

def new_customer(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/customer/customer-new.html')
    context = {
        'customer': customer,
    }
    return HttpResponse(template.render(context, request))
