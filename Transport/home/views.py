from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Order
from .models import Customer
from .models import Employee
from .forms import PackageNewForm, CustomerNewForm
from .forms import EmployeeNewForm
from elasticsearch_dsl import Q
from django.core.cache import cache 
from django.views.decorators.cache import cache_page
from T_package_Mng.document import PackageDocument
from T_package_Mng.document import EmployeeDocument
from T_package_Mng.document import CustomerDocument
# Create your views here.
@cache_page(60 * 5) # Cache trong 15 phút
def home(request):
    return render(request, 'home/home.html')
#package
def clear_cache(request):
    cache.delete('package') # Xóa cache theo key

def package(request):
    package = cache.get('package')
    if not package:
        # Nếu không có, tạo dữ liệu và lưu vào cache 
        package = Order.objects.all()  
        cache.set('package', package, timeout=60*3) # Lưu cache trong 60 giây


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


def search_packages(request):
    query = request.GET.get('q', '')  # Lấy từ khóa tìm kiếm từ URL
    results = []  # Khởi tạo danh sách kết quả tìm kiếm

    print('---------------------------------------', query)

    if query:  # Nếu có từ khóa tìm kiếm
        q = Q("multi_match", query=query, fields=["name", "note"])  # Tạo query tìm kiếm

        # Thực hiện tìm kiếm trên Elasticsearch
        search = PackageDocument.search().query(q)
        results = search.execute()  # Lấy kết quả tìm kiếm từ Elasticsearch

        print('=========================================================', results)

    return render(request, 'home/package/search_results.html', {'results': results,'query': query })



def delete_package(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/package/package-delete.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def new_package(request):
    if request.method == 'POST':
        form = PackageNewForm(request.POST)
        print(form)
        if form.is_valid():
            return HttpResponseRedirect("/package/")

    template = loader.get_template('home/package/package-new.html')
    context = {
        
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
    employee = Employee.objects.filter(id=1).first() 
    template = loader.get_template('home/employee/employee-delete.html')
    context = {
        'employee': employee,
    }
    return HttpResponse(template.render(context, request))

def new_employee(request):
    if request.method == 'POST':
        form = EmployeeNewForm(request.POST)
        print(form)
        if form.is_valid():
            return HttpResponseRedirect("/employee")

    template = loader.get_template('home/employee/employee-new.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def search_employees(request):
    query = request.GET.get('q', '')  # Lấy từ khóa tìm kiếm từ URL
    results = []  # Khởi tạo danh sách kết quả tìm kiếm

    print('---------------------------------------', query)

    if query:  # Nếu có từ khóa tìm kiếm
        q = Q("multi_match", query=query, fields=["name"])  # Tạo query tìm kiếm

        # Thực hiện tìm kiếm trên Elasticsearch
        search = EmployeeDocument.search().query(q)
        results = search.execute()  # Lấy kết quả tìm kiếm từ Elasticsearch

        print('=========================================================', results)

    return render(request, 'home/employee/search_results.html', {'results': results,'query': query })

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
    customer = Customer.objects.filter(id=1).first() 
    template = loader.get_template('home/customer/customer-delete.html')
    context = {
        'customer': customer,
    }
    return HttpResponse(template.render(context, request))

def new_customer(request):
    if request.method == 'POST':
        form = CustomerNewForm(request.POST)
        print(form)
        if form.is_valid():
            return HttpResponseRedirect("/customer")

    template = loader.get_template('home/customer/customer-new.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def search_customers(request):
    query = request.GET.get('q', '')  # Lấy từ khóa tìm kiếm từ URL
    results = []  # Khởi tạo danh sách kết quả tìm kiếm

    print('---------------------------------------', query)

    if query:  # Nếu có từ khóa tìm kiếm
        q = Q("multi_match", query=query, fields=["name"])  # Tạo query tìm kiếm

        # Thực hiện tìm kiếm trên Elasticsearch
        search = CustomerDocument.search().query(q)
        results = search.execute()  # Lấy kết quả tìm kiếm từ Elasticsearch

        print('=========================================================', results)

    return render(request, 'home/customer/search_results.html', {'results': results,'query': query })