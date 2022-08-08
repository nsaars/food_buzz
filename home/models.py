from datetime import datetime

from django.db import models
from django.db.models import Q
from django.urls import reverse

from shop.models import Product, ProductImage


class TodaySpecialProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.product.slug})

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "Продукт 'speacial today'"
        verbose_name_plural = "Продукты 'speacial today'"
        ordering = ['-date']

    @staticmethod
    def get_today_special_products_with_images():
        product_ids = [product_id['product__id'] for product_id in TodaySpecialProduct.objects.filter(date=datetime.today()).values('product__id')]
        return Product.get_products_with_images(product_ids)
