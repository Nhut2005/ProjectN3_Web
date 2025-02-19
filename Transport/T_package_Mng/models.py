from django.db import models

# Create your models here.
class Employee(models.Model):
	name = models.CharField(max_length=255)
	gender = models.CharField(max_length=255)
	birth_day = models.DateField()
	email = models.CharField(max_length=255)
	phone = models.CharField(max_length=15, default="Không có số")
	Role = models.CharField(max_length=255)
	active = models.BooleanField(default=True)

class Customer(models.Model):
	name = models.CharField(max_length=255)
	gender = models.CharField(max_length=255)
	birth_day = models.DateField()
	email = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	active = models.BooleanField(default=True)
	# def __str__(self):
	# 	    return f"{self.name} {self.gender}"
class Order(models.Model):
	name =models.CharField(max_length=255)
	size = models.CharField(max_length=255)
	quantity = models.IntegerField()
	origin = models.CharField(max_length=255)
	ship_service = models.CharField(max_length=255)
	price = models.FloatField()
	note = models.CharField(max_length=255)
	def __str__(self):
		return f"{self.name} {self.size}"
class inforTransport(models.Model):
	method = models.CharField(max_length=255)
	ìnforcompany = models.CharField(max_length=255)
	inforprices = models.FloatField()
	service = models.CharField(max_length=255)
	

class ServicePrice(models.Model):
    service_type = models.CharField(max_length=100)
    distance = models.CharField(max_length=100)
    delivery_time = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_type
	
	
