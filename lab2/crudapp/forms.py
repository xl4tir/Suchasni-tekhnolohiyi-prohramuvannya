from django import forms
from .models import Orders

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
        labels = {
            'oid': 'ID замовлення',
            'fname': "Ім'я",
            'lname': "Прізвище",
            'price': 'Сума (₴)',
            'mail': 'Електронна пошта',
            'addr': 'Адреса доставки',
        }
        widgets = {
            'oid': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наприклад, 101',
                'min': '1',
            }),
            'fname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Ім'я замовника",
            }),
            'lname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Прізвище замовника",
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наприклад, 1500.50',
                'step': '0.01',
                'min': '0',
            }),
            'mail': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@email.com',
            }),
            'addr': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть повну адресу',
                'rows': 3,
            }),
        }
