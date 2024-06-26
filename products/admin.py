from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('sku',)
    list_display = (
        'name',
        'price',
        'sku',
    )
    ordering = ('name', 'sku', 'price',)
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
