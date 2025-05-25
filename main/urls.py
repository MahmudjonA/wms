# main/urls.py

from django.urls import path
from .views import employee_login_view, employee_logout_view, dashboard

urlpatterns = [
    path('login/', employee_login_view, name='login'),
    path('logout/', employee_logout_view, name='logout'),
    path('', dashboard, name='dashboard'),
]
