from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_cart',
              'stripe_pid', 'status', 'tracking_number')
    list_display = ('order_number', 'status', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total')

    list_filter = ('status',)

    ordering = ('-date',)
    
    actions = ['mark_as_shipped', 'mark_as_delivered', 'mark_as_cancelled']

    def mark_as_shipped(self, request, queryset):
        queryset.update(status='S')  # Update status to 'Shipped'
    mark_as_shipped.short_description = "Mark selected orders as shipped"

    def mark_as_delivered(self, request, queryset):
        queryset.update(status='D')  # Update status to 'Delivered'
    mark_as_delivered.short_description = "Mark selected orders as delivered"

    def mark_as_cancelled(self, request, queryset):
        queryset.update(status='C')  # Update status to 'Cancelled'
    mark_as_cancelled.short_description = "Mark selected orders as cancelled"

admin.site.register(Order, OrderAdmin)