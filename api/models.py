from django.db import models

# Create your models here.

class Employee(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	gender = models.CharField(max_length=50)
	address = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
