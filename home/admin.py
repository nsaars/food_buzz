from django.contrib import admin
from django.contrib.admin import register
from .models import TodaySpecialProduct


@register(TodaySpecialProduct)
class TodaySpecialProductAdmin(admin.ModelAdmin):
    pass
