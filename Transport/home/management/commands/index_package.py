from django.core.management.base import BaseCommand
from elasticsearch_dsl import Document, Text, Float
from elasticsearch_dsl.connections import connections
from T_package_Mng.models import Order
from T_package_Mng.models import Employee
from T_package_Mng.models import Customer
from T_package_Mng.document import PackageDocument 
from T_package_Mng.document import EmployeeDocument 
from T_package_Mng.document import CustomerDocument  # Đảm bảo rằng PackageDocument đúng
class Command(BaseCommand):
    help = 'Index course data into Elasticsearch'  # Đã sửa cú pháp help

    def handle(self, *args, **kwargs): 
        packages = Employee.objects.all()  # Lấy tất cả đối tượng Order
        
        for package in packages:
            # Tạo tài liệu Elasticsearch cho mỗi Order
            doc = PackageDocument(
                meta={'id': package.id},
                name=package.name,
                note=package.note,
                # created_at=package.created_at,  # Nếu cần thiết, bạn có thể bỏ comment dòng này
            )
            doc.save()  # Lưu tài liệu vào Elasticsearch
        
        # In ra số lượng bản ghi đã được index
        self.stdout.write(self.style.SUCCESS(f'Successfully indexed {packages.count()} packages.'))

class Command(BaseCommand):
    help = 'Index course data into Elasticsearch'  # Đã sửa cú pháp help

    def handle(self, *args, **kwargs): 
        employees = Employee.objects.all()  # Lấy tất cả đối tượng Order
        
        for employee in employees:
            # Tạo tài liệu Elasticsearch cho mỗi Order
            doc = EmployeeDocument(
                meta={'id': employee.id},
                name=employee.name,
                # created_at=package.created_at,  # Nếu cần thiết, bạn có thể bỏ comment dòng này
            )
            doc.save()  # Lưu tài liệu vào Elasticsearch
        
        # In ra số lượng bản ghi đã được index
        self.stdout.write(self.style.SUCCESS(f'Successfully indexed {employees.count()} employees.'))

class Command(BaseCommand):
    help = 'Index course data into Elasticsearch'  # Đã sửa cú pháp help

    def handle(self, *args, **kwargs): 
        customers = Customer.objects.all()  # Lấy tất cả đối tượng Order
        
        for customer in customers:
            # Tạo tài liệu Elasticsearch cho mỗi Order
            doc = CustomerDocument(
                meta={'id': customer.id},
                name=customer.name,
                # created_at=package.created_at,  # Nếu cần thiết, bạn có thể bỏ comment dòng này
            )
            doc.save()  # Lưu tài liệu vào Elasticsearch
        
        # In ra số lượng bản ghi đã được index
        self.stdout.write(self.style.SUCCESS(f'Successfully indexed {customers.count()} customers.'))