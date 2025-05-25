from django.db import models
from product.models import Product
from location.models import Location

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory_records')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='inventory_records')
    quantity = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        unique_together = ('product', 'location')

    def __str__(self):
        return f"{self.product.sku} @ {self.location}: {self.quantity}"