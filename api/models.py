from django.db import models

# Create your models here.

class Customer(models.Model):

    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    vehicle_no=models.CharField(max_length=200)
    running_km=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name 

    
