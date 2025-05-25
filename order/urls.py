from django.urls import path
from .views import purchaseorder_list, purchaseorder_update, purchaseorder_delete

urlpatterns = [
    path('', purchaseorder_list, name='purchaseorder_list'),
    path('update/<int:pk>/', purchaseorder_update, name='purchaseorder_update'),
    path('delete/<int:pk>/', purchaseorder_delete, name='purchaseorder_delete'),
]
