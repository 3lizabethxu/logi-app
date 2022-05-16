from django.forms import ModelForm
from dataclasses import field

import inventory_app.models

class ProductForm(ModelForm):
    class Meta:
        model = inventory_app.models.Product
        fields = '__all__'

class WarehouseForm(ModelForm):
    class Meta:
        model = inventory_app.models.Warehouse
        fields = '__all__'
        