from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category
from inventory.models import Inventory

class ProductForm(forms.ModelForm):
    quantity = forms.IntegerField(label='Quantity', required=True)

    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'description',
            'price',
            'image',
            'is_addon',
        ]
        widgets = {
            'image': CustomClearableFileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        if self.instance.pk:
            product_inventory = Inventory.objects.filter(product=self.instance)
            if product_inventory.exists():
                initial_quantity = product_inventory.first().quantity
            else:
                initial_quantity = 0
            self.fields['quantity'].initial = initial_quantity
            self.fields['is_addon'].initial = self.instance.is_addon

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            product_inventory, created = Inventory.objects.get_or_create(product=instance)
            product_inventory.quantity = self.cleaned_data['quantity']
            product_inventory.save()
        return instance