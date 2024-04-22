from django.contrib import admin
from .models import Inventory, AddOnInventory

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')
    search_fields = ('product__name',)
    list_per_page = 20


class AddOnInventoryAdmin(admin.ModelAdmin):
    list_display = ('addon', 'quantity')
    search_fields = ('addon__name',)
    list_per_page = 20

admin.site.register(Inventory, InventoryAdmin)
admin.site.register(AddOnInventory, AddOnInventoryAdmin)
