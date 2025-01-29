from django.core.management.base import BaseCommand
from elasticsearch_dsl import Document, Text, Float
from elasticsearch_dsl.connections import connections
from T_package_Mng.models import Order
from T_package_Mng.document import PackageDocument  # Đảm bảo rằng PackageDocument đúng

class Command(BaseCommand):
    help = 'Index course data into Elasticsearch'  # Đã sửa cú pháp help

    def handle(self, *args, **kwargs): 
        packages = Order.objects.all()  # Lấy tất cả đối tượng Order
        
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
