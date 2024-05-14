from django.contrib import admin, messages
from django.core.mail import send_mail
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart',
                       'stripe_pid', 'status')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_cart',
              'stripe_pid', 'status', 'tracking_number')

    list_display = ('order_number', 'status', 'full_name',
                    'grand_total', 'date')

    list_filter = ('status',)

    ordering = ('-date',)
    
    search_fields = ('order_number', 'full_name', 'email', 'date')
    
    actions = ['mark_as_shipped', 'mark_as_delivered', 'mark_as_cancelled']

    def send_status_change_email(self, request, queryset, new_status):
        for order in queryset:
            subject = f"Order #{order.order_number} Status Update"
            message = f"Dear {order.full_name},\n\nYour order with tracking number {order.tracking_number} has been updated to '{new_status}' status.\n\nThank you for shopping with us!\n\nBest regards,\nThe Store Team"
            send_mail(subject, message, 'your_email@example.com', [order.email])

    def mark_as_shipped(self, request, queryset):
        for order in queryset:
            if not order.tracking_number:  # If tracking number is not set
                # Show a message to the admin in red
                self.message_user(request, f"Tracking number not set for Order #{order.order_number}. Please set it manually.", level=messages.ERROR)
            else:
                order.status = 'S'  # Update status to 'Shipped'
                order.save()
                self.send_status_change_email(request, [order], 'Shipped')
    mark_as_shipped.short_description = "Mark selected orders as shipped"

    def mark_as_delivered(self, request, queryset):
        for order in queryset:
            order.status = 'D'  # Update status to 'Delivered'
            order.save()
            self.send_status_change_email(request, [order], 'Delivered')
    mark_as_delivered.short_description = "Mark selected orders as delivered"

    def mark_as_cancelled(self, request, queryset):
        for order in queryset:
            order.status = 'C'  # Update status to 'Cancelled'
            order.save()
            self.send_status_change_email(request, [order], 'Cancelled')
    mark_as_cancelled.short_description = "Mark selected orders as cancelled"

admin.site.register(Order, OrderAdmin)
