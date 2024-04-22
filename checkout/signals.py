from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem
from products.models import Product
from inventory.models import Inventory


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
    

@receiver(post_delete, sender=OrderLineItem)
def restore_inventory(sender, instance, **kwargs):
    """
    Restore inventory upon order line item deletion
    """
    product = instance.product
    inventory = Inventory.objects.get(product=product)
    quantity_sold = instance.quantity
    inventory.quantity += quantity_sold
    inventory.save()

@receiver(post_save, sender=OrderLineItem)
def update_inventory(sender, instance, created, **kwargs):
    """
    Update inventory upon order line item creation
    """
    print('update_inventory signal received!')
    if created:
        product = instance.product
        inventory = Inventory.objects.get(product=product)
        quantity_sold = instance.quantity
        inventory.quantity -= quantity_sold
        inventory.save()
