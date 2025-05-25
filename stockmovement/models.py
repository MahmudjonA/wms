from django.db import models
from product.models import Product
from location.models import Location
from employee.models import Employee


class StockMovement(models.Model):
    IN = 'IN'
    OUT = 'OUT'
    MOVEMENT_TYPE_CHOICES = [
        (IN, 'Inbound'),
        (OUT, 'Outbound'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='movements')
    from_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name='movements_out')
    to_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name='movements_in')
    quantity = models.IntegerField()
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    performed_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    reference = models.CharField(max_length=100, blank=True, null=True, help_text="PO/Order/Shipment ref")

    def __str__(self):
        return f"{self.get_movement_type_display()}: {self.product.sku} x{self.quantity}"
    