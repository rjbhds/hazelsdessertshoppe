from django.forms import ModelForm, TextInput, Textarea, Select, CheckboxInput, FileInput
from hazelsdessertshoppe.models import Product
from django.forms.widgets import NumberInput

class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'category',
            'image',
            'not_in_season'
        ]
    
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Dessert name...',
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'description': Textarea(
                attrs = {
                    'cols': 80,
                    'rows': 6,
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'price': NumberInput(
                attrs={
                    'placeholder': '9.99...',
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'category': Select(
                attrs={
                    'class': 'form-control select-placeholder',
                    'required': 'required',
                }
            ),
            'image': FileInput(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'not_in_season': CheckboxInput(
                attrs={
                    'class': 'form-control custom-form-checkbox custom-form-checkbox-round',
                }
            )
        }