from django.urls import path

from . import views


urlpatterns = [
    path("items", views.items, name="items"),
    path("orders", views.orders, name="orders"),
    path("order_batches", views.order_batches, name="order_batches"),
]
