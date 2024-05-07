from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'rating',
    )
    ordering = ('name', 'sku', 'price', 'rating',)
    search_fields = ('sku', 'name')
    list_per_page = 20


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    search_fields = ('friendly_name', 'name')
    list_per_page = 20


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
