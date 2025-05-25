from django.db import models
from warehouse.models import Warehouse

class Location(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='locations')
    zone = models.CharField(max_length=50)
    aisle = models.CharField(max_length=50)
    rack = models.CharField(max_length=50)
    bin = models.CharField(max_length=50)

    class Meta:
        unique_together = ('warehouse', 'zone', 'aisle', 'rack', 'bin')

    def __str__(self):
        return f"{self.warehouse.code}-{self.zone}-{self.aisle}-{self.rack}-{self.bin}"