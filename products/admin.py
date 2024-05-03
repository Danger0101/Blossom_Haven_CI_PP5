from django.contrib import admin
from .models import Product, Category
from inventory.models import Inventory


class InventoryInline(admin.StackedInline):
    model = Inventory
    can_delete = False
    verbose_name_plural = 'Inventory'


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
    inlines = (InventoryInline,)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    search_fields = ('friendly_name', 'name')
    list_per_page = 20


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
