from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Order
from .models import Customer
from .models import Employee
from .forms import PackageNewForm, CustomerNewForm
from .forms import EmployeeNewForm
from django.contrib.auth import authenticate, login
from .forms import PackageForm  # Đảm bảo import form
from .models import ServicePrice
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.cache import cache 
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(60 * 5) # Cache trong 15 phút
def home(request):
    return render(request, 'home/base.html')
#package
def clear_cache(request):
    cache.delete('package') # Xóa cache theo key


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("account")  # Chuyển hướng về trang chính sau khi đăng nhập
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng.")
            return redirect("login_user")

    return render(request, "home/login.html")



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

def create_package(request):
    if request.method == "POST":
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('package')  # Chuyển hướng đến danh sách
    else:  # Đúng: else thụt lề chính xác
        form = PackageForm()  # Đúng: thụt lề đúng với else
    
        return render(request, 'home/package/package-edit.html', {'form': form})



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

def view_account(request):
    return render(request, 'home/account.html')

def my_order(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/package/myorders.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def my_addresses(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/package/address-book.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def my_voucher(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/package/voucher.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def my_setting(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/package/setting.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def my_blog(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/package/blog.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def my_question(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/package/question.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))


def my_contact(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/package/contact.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def view_manager(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/manager/quanly.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def view_shipmenu(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/manager/don_van_chuyen.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def view_shipprocess(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/manager/shippingprocess.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def view_pricelist(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/manager/banggia.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def view_dashboard(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/manager/baocao.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def view_feedback(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/manager/danhgia.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def view_profile(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/manager/hskh.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))


def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Mật khẩu nhập lại không khớp.")
            return redirect("register_user")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Tên đăng nhập đã tồn tại.")
            return redirect("register_user")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email đã được sử dụng.")
            return redirect("register_user")

        # Tạo tài khoản mới
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Đăng ký thành công! Hãy đăng nhập.")
        return redirect("login_user")

    return render(request, "home/register.html")


def view_dichvu(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/gioithieu.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def view_tkprofile(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/profile.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))


# views.py
from django.shortcuts import render, redirect
from .models import ServicePrice

def price_list(request):
    prices = ServicePrice.objects.all()  # Lấy tất cả dữ liệu từ model
    return render(request, 'home/pricePage.html', {'prices': prices})


def view_congty(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/congty.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))

def view_nhanvien(request):
    package = Order.objects.filter(id=1).first() 
    template = loader.get_template('home/manager/nhanvien.html')
    context = {
        'package': package,
    }
    return HttpResponse(template.render(context, request))