from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product

User = get_user_model()

class Review(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='reviews',
        null=True,
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        related_name='reviews',
        null=True,
        on_delete=models.CASCADE)
    user_rating = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0),MaxValueValidator(5)])
    review_title = models.CharField(
        max_length=100,
        null=True,
        blank=True)
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    @property
    def product_avg_rating(self):
        return self.product.review_set.aggregate(Avg('user_rating'))['user_rating__avg']
