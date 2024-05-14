from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('date', 'edit_date', 'user', 'product', 'review_title', 'user_rating', 'review')
    
    list_display = (
        'product',
        'user',
        'review_title',
        'user_rating',
        'date',
        'edit_date',
    )
    ordering = ('date', 'user_rating', 'product', 'user', 'review_title', 'edit_date',)
    sortable_by = ('date', 'user_rating', 'product', 'user', 'review_title', 'edit_date',)
    search_fields = ('product__name', 'user__username', 'review_title', 'user_rating', 'date', 'edit_date',)
    list_filter = ('product', 'user', 'review_title', 'user_rating', 'date', 'edit_date',)
    list_per_page = 20
    
admin.site.register(Review, ReviewAdmin)