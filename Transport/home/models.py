from django.db import models
from T_package_Mng.models import Employee
from T_package_Mng.models import Customer
from T_package_Mng.models import Order
from django.db import models

# Create your models here.

class Package(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name