from django.views.generic import DetailView
from django.views.generic.list import ListView

from cart.cart import Cart
from shop.models import Product, ProductImage
from home.utils import DataMixin


class ShopListView(DataMixin, ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_products'] = list(cart_product['product'] for cart_product in Cart(self.request))
        return dict(self.get_page_context() | context)


class ProductDetailView(DataMixin, DetailView):
    model = Product
    template_name = 'shop/product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = ProductImage.objects.filter(_product__slug=self.kwargs['product_slug'])
        print(context['images'])
        return dict(self.get_page_context() | context)