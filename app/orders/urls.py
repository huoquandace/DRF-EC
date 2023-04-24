from django.urls import path
from orders.views import OrderAPI, OrderIdAPI

urlpatterns = [
    path("", OrderAPI.as_view(), name="order"),
    path("<int:pk>/", OrderIdAPI.as_view(), name="order_id"),
]
