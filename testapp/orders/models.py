from django.db import models


class Item(models.Model):
    """An item."""

    name = models.CharField("Item", max_length=255)

    def __str__(self) -> str:
        return f"{self.name} - ({self.id})"
    
    class Meta:
        verbose_name="Item"


class Order(models.Model):
    """An order for an item."""

    class OrderStatus(models.IntegerChoices):
        RECEIVED = 0, "Received"
        PROCESSING = 1, "Processing"
        FULFILLED = 2, "Fulfilled"
    
    item = models.ForeignKey(Item, verbose_name="Item", related_name="orders", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Quantity", default=0)
    status = models.PositiveIntegerField("Status", choices=OrderStatus.choices, default=OrderStatus.RECEIVED)
    created_dt = models.DateTimeField("Created Datetime", auto_now_add=True, editable=False)    
    completed_dt = models.DateTimeField("Completed Datetime", auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return f"Order ({self.id}) for item {self.item} | Quantity: {self.quantity} | At: {self.created_dt}"

    class Meta:
        verbose_name = "Order"


class OrderBatch(models.Model):
    """A batch of orders for items."""

    class OrderBatchStatus(models.IntegerChoices):
        RECEIVED = 0, "Received"
        PROCESSING = 1, "Processing"
        FULFILLED = 2, "Fulfilled"

    status = models.PositiveIntegerField("Status", choices=OrderBatchStatus.choices, default=OrderBatchStatus.RECEIVED)
    orders = models.ManyToManyField(Order, verbose_name="Orders", related_name="+")
    total_items = models.PositiveIntegerField("Total items", default=0)
    created_dt = models.DateTimeField("Created Datetime", auto_now_add=True, editable=False)    
    completed_dt = models.DateTimeField("Completed Datetime", auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "Order Batch"
        verbose_name_plural = "Order Batches"
