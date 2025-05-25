from django.urls import path
from .views import order_item_list, order_item_update, order_item_delete

urlpatterns = [
    path('', order_item_list, name='order_item_list'),
    path('update/<int:pk>/', order_item_update, name='order_item_update'),
    path('delete/<int:pk>/', order_item_delete, name='order_item_delete'),
]
