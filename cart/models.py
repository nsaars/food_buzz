from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse_lazy

from shop.models import Product


class AvailableCity(models.Model):
    title = models.CharField(max_length=31)
    shipping_price = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Доступный город'
        verbose_name_plural = 'Доступные города'
        ordering = ['title']


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderDetails(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'")

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    shipping_city = models.ForeignKey(AvailableCity, on_delete=models.PROTECT)
    shipping_address = models.CharField(max_length=127)
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    shipping_price = models.IntegerField()
    cart_total = models.IntegerField()
    order_date = models.DateTimeField()

    def __str__(self):
        return f'{self.order.user.username} {self.order_date}'

    class Meta:
        verbose_name = 'Детали Заказа'
        verbose_name_plural = 'Детали Заказов'
        ordering = ['order_date']


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    quantity = models.IntegerField()

    def get_absolute_url(self):
        return reverse_lazy('product', kwargs={'product_slug': self.product.slug})

    def __str__(self):
        return f'{self.order.user.username} - {self.product.title}'

    class Meta:
        verbose_name = 'Продукт из заказа'
        verbose_name_plural = 'Продукты из заказов'
        ordering = ['product']

