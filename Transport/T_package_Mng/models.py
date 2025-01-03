from django.db import models

# Create your models here.
class Employee(models.Model):
	name = models.CharField(max_length=255)
	gender = models.BooleanField()
	birth_day = models.DateField()
	email = models.CharField(max_length=255)
	Role = models.CharField(max_length=255)

class Customer(models.Model):
	name = models.CharField(max_length=255)
	gender = models.BooleanField()
	birth_day = models.DateField()
	email = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)

class Order(models.Model):
	name =models.CharField(max_length=255)
	size = models.CharField(max_length=255)
	quantity = models.FloatField()
	origin = models.CharField(max_length=255)
	ship_service = models.CharField(max_length=255)
	price = models.FloatField()
	note = models.CharField(max_length=255)

	
	
	
