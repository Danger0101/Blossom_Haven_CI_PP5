from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Inventory
from products.models import Product

# Signals for Product model
@receiver(post_save, sender=Product)
def create_product_inventory(sender, instance, created, **kwargs):
    """
    Create an inventory entry for the product when it is created.
    """
    if created:
        print('Creating inventory entry for product')
        Inventory.objects.create(product=instance)

@receiver(post_save, sender=Product)
def save_product_inventory(sender, instance, **kwargs):
    """
    Save the inventory entry whenever the product is saved.
    """
    print('Saving inventory entry for product')
    instance.inventory.save()
