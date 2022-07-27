from django.contrib import admin
from django.contrib.admin import register

from shop.models import Product, ProductImage, Category


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass
