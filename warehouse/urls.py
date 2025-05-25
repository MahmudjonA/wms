from django.urls import path
from .views import (
    warehouse_list,
    warehouse_update,
    warehouse_delete,
)

urlpatterns = [
    path('', warehouse_list, name='warehouse_list'),
    path('update/<int:pk>/', warehouse_update, name='warehouse_update'),
    path('delete/<int:pk>/', warehouse_delete, name='warehouse_delete'),
]
