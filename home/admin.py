from django.contrib import admin
from django.contrib.admin import register
from .models import Page, TodaySpecialProduct


@register(Page)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@register(TodaySpecialProduct)
class TodaySpecialProductAdmin(admin.ModelAdmin):
    pass
