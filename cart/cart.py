from decimal import Decimal
from django.conf import settings
from django.db.models import Q

from shop.models import Product, ProductImage


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = int(quantity)
        else:
            self.cart[product_id]['quantity'] += int(quantity)
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_product_total_price(self, product):
        cart_product = self.cart[str(product.id)]
        return Decimal(cart_product['price']) * cart_product['quantity']

    def get_total_price(self):

        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        products_with_image = self.get_cart_products_with_images()
        for product, product_image in products_with_image:
            self.cart[str(product.id)]['product'] = product
            self.cart[str(product.id)]['image'] = product_image

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def get_cart_products_with_images(self):
        product_ids = self.cart.keys()
        return Product.get_products_with_images(product_ids)