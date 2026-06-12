from django.db import models
from apps.common.models import BaseModel
from apps.products.models import Product


class Order(BaseModel):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"Order: {self.id} - {self.total_price} so'm"
    
class OrderItem(BaseModel):
    
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE,
        related_name='order_items'
    )
    
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='order_items'
    )

    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    
    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
    
    