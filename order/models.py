from django.db import models
from supplier.models import Supplier
from employee.models import Employee


class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='purchase_orders')
    order_date = models.DateField(auto_now_add=True)
    expected_date = models.DateField()
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    reference = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"PO {self.reference}"