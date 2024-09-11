from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.add_customer, name='add_customer'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('edit_customer/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
]
