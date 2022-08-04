from django.db import models
from django.urls import reverse

from shop.models import Product


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
