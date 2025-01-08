from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Order


# Create your views here.

def home (request):
    return render(request, 'home/home.html')

def package(request):
    package = Order.objects.all()  
    template = loader.get_template('home/package.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def edit_package(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/package-edit.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

