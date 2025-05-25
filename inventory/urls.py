# inventory/urls.py

from django.urls import path
from .views import inventory_list, inventory_update, inventory_delete

urlpatterns = [
    path('', inventory_list, name='inventory_list'),
    path('update/<int:pk>/', inventory_update, name='inventory_update'),
    path('delete/<int:pk>/', inventory_delete, name='inventory_delete'),
]
