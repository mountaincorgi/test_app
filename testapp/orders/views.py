from django.http import HttpResponse
from django.template import loader

from .models import Item, Order, OrderBatch


def items(request):
    all_items = Item.objects.order_by("id")
    template = loader.get_template("orders/items.html")
    context = {"items": all_items}
    return HttpResponse(template.render(context, request))


def orders(request):
    all_orders = Order.objects.order_by("id")
    template = loader.get_template("orders/orders.html")
    context = {"orders": all_orders}
    return HttpResponse(template.render(context, request))


def order_batches(request):
    all_order_batches = OrderBatch.objects.order_by("id")
    template = loader.get_template("orders/order_batches.html")
    context = {"orders": all_order_batches}
    return HttpResponse(template.render(context, request))
