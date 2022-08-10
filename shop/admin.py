from django.contrib import admin
from django.contrib.admin import register
from django.utils.safestring import mark_safe

from shop.models import Product, ProductImage, Category


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug', 'image', 'menu_order', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'category', 'title', 'slug', 'price', 'has_image', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


@register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'get_html_image')
    list_display_links = ('id',)
    fields = ('product', 'image', 'get_html_image')
    readonly_fields = ('get_html_image', )
    def get_html_image(self, object):
        return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_image.short_description = "Миниатюра"
