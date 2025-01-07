from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Employee


# Create your views here.

def home (request):
    return render(request, 'home/home.html')

def employee(request):
    employee = Employee.objects.all()  # Đảm bảo thụt lề đúng
    template = loader.get_template('home/employee.html')
    context = {
        'employee': employee,
    }
    return HttpResponse(template.render(context, request))

def edit_employee(request):
    employee = Employee.objects.get(id=1)  # Đảm bảo thụt lề đúng
    template = loader.get_template('home/employee-edit.html')
    context = {
        'employee': employee,
    }
    return HttpResponse(template.render(context, request))

