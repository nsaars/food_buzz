from django.urls import path
from .views import CartView, change_quantity, add_to_cart, remove_from_cart, change_city

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('change-quantity/', change_quantity, name='change_qty'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/', remove_from_cart, name='remove_from_cart'),
    path('change-city/', change_city, name='change_city'),
]