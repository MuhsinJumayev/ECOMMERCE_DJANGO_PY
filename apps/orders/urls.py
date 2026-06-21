from django.urls import path
from apps.orders.api_endpoints.orders.OrderList.views import order_list

urlpatterns = [
    path('orders/', order_list, name='order-list'),
]