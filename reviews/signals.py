from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Review

@receiver(post_save, sender=Review)
def update_product_rating(sender, instance, created, **kwargs):
    if created or instance.user_rating != instance._state.fields_cache['user_rating']:
        instance.product.rating = instance.product.calculate_average_rating()
        instance.product.save()
