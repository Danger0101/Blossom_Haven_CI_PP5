from django.contrib import admin
from django.conf import settings
from cloudinary import uploader
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

    def save_model(self, request, obj, form, change):
        # Check if a new image is uploaded
        if 'image' in request.FILES:
            # Upload new image to Cloudinary
            image = request.FILES['image']
            uploaded_image = uploader.upload(image, folder=settings.CLOUDINARY_FOLDER_NAME)
            obj.image = uploaded_image.url
        super().save_model(request, obj, form, change)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
