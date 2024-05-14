from django.db import models
from cloudinary.models import CloudinaryField
import uuid
from django.db.models import Avg

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ManyToManyField(Category, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True)
    is_addon = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.sku or Product.objects.filter(sku=self.sku).exists():
            self.sku = str(uuid.uuid4()).replace('-', '').upper()[:10]
        super().save(*args, **kwargs)
