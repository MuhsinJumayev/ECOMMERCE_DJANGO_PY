from django.db import models
from apps.common.models import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='products', null=True, blank=True
    )
    
    def __str__(self):
        return self.name