from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category
from inventory.models import Inventory


class ProductForm(forms.ModelForm):
    quantity = forms.IntegerField(label='Quantity', required=True)
    is_addon = forms.BooleanField(label='Is Addon', required=False)

    class Meta:
        model = Product
        fields = [
            'sku',
            'category',
            'name',
            'description',
            'price',
            'rating',
            'image',
            'image_url',
            'is_addon',
        ]

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        # Fetch initial quantity only if the instance has been saved
        if self.instance.pk:
            product_inventory = Inventory.objects.filter(product=self.instance)
            if product_inventory.exists():
                initial_quantity = product_inventory.first().quantity
            else:
                initial_quantity = 0
            self.fields['quantity'].initial = initial_quantity

            # Set initial value for is_addon field
            self.fields['is_addon'].initial = self.instance.is_addon

    def save(self, commit=True):
        # Save inventory data along with product
        instance = super().save(commit=False)
        if commit:
            instance.save()
            # Ensure that the product instance is saved before accessing inventory
            product_inventory, created = Inventory.objects.get_or_create(product=instance)
            product_inventory.quantity = self.cleaned_data['quantity']
            product_inventory.save()
        return instance
