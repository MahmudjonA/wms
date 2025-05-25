from django.urls import path
from .views import (
    location_list,
    location_update,
    location_delete,
)

urlpatterns = [
    path('', location_list, name='location_list'),
    path('update/<int:pk>/', location_update, name='location_update'),
    path('delete/<int:pk>/', location_delete, name='location_delete'),
]
