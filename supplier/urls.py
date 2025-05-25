# supplier/urls.py
from django.urls import path
from .views import supplier_list, supplier_delete, SupplierUpdateView

urlpatterns = [
    path('', supplier_list, name='supplier_list'),
    path('create/', supplier_list, name='supplier_create'),
    path('update/<int:pk>/', SupplierUpdateView.as_view(), name='supplier_update'),  # POST orqali update
    path('delete/<int:pk>/', supplier_delete, name='supplier_delete'),  # POST orqali delete
]
