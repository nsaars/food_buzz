from django.db import models
from django.db.models import Q
from django.db.models.signals import post_init, post_save
from django.dispatch import receiver
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, db_index=True)
    image = models.ImageField(upload_to='category', blank=True)
    menu_order = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    @staticmethod
    def get_products_with_image_by_category():
        products = Product.get_products_with_images()
        products_by_category = {category: list() for category in Category.objects.all().order_by('menu_order')}
        for product, product_image in products:
            products_by_category[product.category] += [(product, product_image)]
        return products_by_category.items()


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, db_index=True)
    price = models.IntegerField()
    description = models.TextField()
    has_image = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    def __str__(self):
        return f"{self.title} - {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["title"]

    @staticmethod
    def get_products_with_images(product_ids=None):
        if product_ids is not None:
            products = tuple(Product.objects.filter(Q(has_image=True) & Q(id__in=product_ids)).order_by('id').select_related('category'))
            product_images = tuple(
                ProductImage.objects.filter(product_id__in=product_ids).order_by('product_id').distinct('product'))
        else:
            products = tuple(Product.objects.filter(has_image=True).order_by('id').select_related('category'))
            product_images = tuple(
                ProductImage.objects.filter().order_by('product_id').distinct('product'))
        return [(products[p], product_images[p]) for p in range(len(products))]


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"
        ordering = ["product"]

    def __str__(self):
        return f"{self.product}"


@receiver(post_save, sender=ProductImage)
def create_product_image(sender, instance, created, *args, **kwargs):
    if created:
        Product.objects.filter(id=instance.product.id).update(has_image=True)
