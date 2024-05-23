from django.contrib import admin
from .models import Inventory


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')
    search_fields = ('product__name',)
    list_per_page = 20


admin.site.register(Inventory, InventoryAdmin)
