from .models import *
from django.forms import ModelForm, TextInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'manufacturer', 'weight', 'price']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
            'manufacturer': TextInput(attrs={
                'class': 'form-control'
            }),
            'weight': TextInput(attrs={
                'class': 'form-control'
            }),
            'price': TextInput(attrs={
                'class': 'form-control'
            })
        }

class CostumerForm(ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'phone_number']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'middle_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'email': TextInput(attrs={
                'class': 'form-control'
            }),
            'phone_number': TextInput(attrs={
                'class': 'form-control'
            })
        }
