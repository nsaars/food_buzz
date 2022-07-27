from django.db import models
from django.urls import reverse

from shop.models import Product


class Page(models.Model):
    order = models.SmallIntegerField(unique=True)
    title = models.CharField(max_length=31)
    slug = models.SlugField(max_length=15)
    show = models.BooleanField(default=1)

    def get_absolute_url(self):
        return reverse(self.slug)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
        ordering = ["order"]


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
