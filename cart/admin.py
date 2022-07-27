from django.contrib import admin
from django.contrib.admin import register

from cart.models import AvailableCity, Order, OrderProduct, OrderDetails


@register(AvailableCity)
class AvailableCityAdmin(admin.ModelAdmin):
    pass


"""@register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    pass


@register(CartDetails)
class CartDetailsAdmin(admin.ModelAdmin):
    pass"""


@register(Order)
class CartAdmin(admin.ModelAdmin):
    pass


@register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    pass


@register(OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    pass
