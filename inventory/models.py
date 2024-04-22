from django.db import models
from products.models import Product, AddOn

class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='inventory')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - Quantity: {self.quantity}"


class AddOnInventory(models.Model):
    addon = models.OneToOneField(AddOn, on_delete=models.CASCADE, related_name='inventory')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.addon.name} - Quantity: {self.quantity}"
