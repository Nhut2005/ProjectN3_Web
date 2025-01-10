from django import forms

class PackageNewForm(forms.Form): 
    name = forms.CharField(label="name", max_length=100)
    size = forms.CharField(label="size", max_length=100)
    quantity = forms.FloatField(label="quantity")
    origin = forms.CharField(label="origin", max_length=100)
    ship_service = forms.CharField(label="ship_service", max_length=100)
    price = forms.FloatField(label="price")  
    note = forms.CharField(label="note", max_length=100)
