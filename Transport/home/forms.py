from django import forms

from .models import Package
class PackageNewForm(forms.Form): 
    name = forms.CharField(label="name", max_length=100)
    size = forms.CharField(label="size", max_length=100)
    quantity = forms.FloatField(label="quantity")
    origin = forms.CharField(label="origin", max_length=100)
    ship_service = forms.CharField(label="ship_service", max_length=100)
    price = forms.FloatField(label="price")  
    note = forms.CharField(label="note", max_length=100)

class CustomerNewForm(forms.Form): 
    name = forms.CharField(label="name", max_length=100)
    gender = forms.CharField(label="gender", max_length=100)
    birth_day = forms.DateField(label="birth_day")
    email = forms.CharField(label="email", max_length=100)
    address = forms.CharField(label="address", max_length=100)
    phone = forms.CharField(label="phone")  
    active = forms.BooleanField(label="active")

class EmployeeNewForm(forms.Form): 
    name = forms.CharField(label="name", max_length=100)
    gender = forms.CharField(label="gender", max_length=100)
    birth_day = forms.DateField(label="birth_day")
    email = forms.CharField(label="email", max_length=100)
    phone = forms.CharField(label="phone", max_length=100)
    Role = forms.CharField(label="Role")  
    active = forms.BooleanField(label="active")
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)



class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'description', 'price']