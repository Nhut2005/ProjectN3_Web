from django.contrib import admin
from .models import Order, Customer, Employee
# Register your models here.
# admin.site.register(Order)
# admin.site.register(Employee)
# admin.site.register(Customer)

class OrderAdmin(admin.ModelAdmin):
  list_display =  ("name", "size", "quantity","origin","ship_service","price", "note")


class EmployeeAdmin(admin.ModelAdmin):
  list_display = ("name", "gender", "birth_day","email","Role","active")

class CustomerAdmin(admin.ModelAdmin):
  list_display = ("name", "gender", "birth_day","email","address","phone", "active")

admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Employee, EmployeeAdmin)