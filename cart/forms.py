from django import forms
from django.forms import TextInput, Select

from cart.models import AvailableCity, OrderDetails


class ShippingDataForm(forms.ModelForm):
    shipping_city = forms.ModelChoiceField(queryset=AvailableCity.objects.all(),
                                           widget=Select(attrs={
                                               'class': 'city-select shipping-city'
                                           }))

    class Meta:
        model = OrderDetails
        fields = ('shipping_city', 'shipping_address', 'phone_number')
        widgets = {
            'shipping_address': TextInput(attrs={
                'placeholder': "Адресс",
                'class': "cart-page-input-text shipping-address",
                'style': "width:550px"
            }),
            'phone_number': TextInput(attrs={
                'placeholder': "Номер телефона",
                'class': "cart-page-input-text phone-number",
                'style': "width:550px"
            })
        }
