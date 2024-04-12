# Using some Botique Ado project code as a base for this project
from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
# End old code
# New addition
class Flower(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
# End of new addition

class Product(models.Model):
    category = models.ManyToManyField('Category', blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    # New addition
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class BouquetSize(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='bouquet_sizes')
    size = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    flowers_required = models.ManyToManyField(Flower, through='BouquetFlowerRequirement')

    def __str__(self):
        return f"{self.product.name} - Size {self.size}"


class BouquetFlowerRequirement(models.Model):
    bouquet_size = models.ForeignKey('BouquetSize', on_delete=models.CASCADE)
    flower = models.ForeignKey('Flower', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.bouquet_size.product.name} - {self.flower.name}: {self.quantity}"


class AddOn(models.Model):
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
# End of new addition