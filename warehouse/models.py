from django.db import models
from employee.models import Employee



class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='warehouses_managed')

    def __str__(self):
        return f"{self.name} ({self.code})"