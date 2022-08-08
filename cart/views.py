from datetime import datetime
from home.utils import DataMixin

from django.urls import reverse_lazy
from cart.cart import Cart

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView

from cart.forms import ShippingDataForm
from cart.models import AvailableCity, OrderDetails, Order

from shop.models import Product, ProductImage


class CartView(DataMixin, FormView):
    template_name = 'cart/cart.html'
    success_url = reverse_lazy('home')
    form_class = ShippingDataForm
    model = OrderDetails

    def form_valid(self, form):
        user = self.request.user
        if not user.is_authenticated:
            return redirect('login')

        form_data = form.cleaned_data
        cart = Cart(self.request)

        shipping_city = AvailableCity.objects.get(title=form_data['shipping_city'])
        order = Order.objects.create(user=user)
        OrderDetails.objects.create(
            order=order, shipping_city=shipping_city, shipping_address=form_data['shipping_address'],
            phone_number=form_data['phone_number'], shipping_price=shipping_city.shipping_price,
            cart_total=cart.get_total_price(), order_date=datetime.today()
        )
        cart.clear()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        context['available_cities'] = AvailableCity.objects.all()
        context['cart_total'] = cart.get_total_price()
        context['cart_products_with_image'] = [(cart_product, cart_product['image']) for cart_product in cart]
        shipping_price = 0
        if 'form' in kwargs:
            shipping_price = kwargs['form'].cleaned_data['shipping_city'].shipping_price
        context['shipping_price'] = shipping_price
        return dict(self.get_page_context() | context)


def change_quantity(request):
    cart = Cart(request)
    data = request.GET
    product = Product.objects.get(title=data['product_title'])
    cart.add(product=product, quantity=data['quantity'], update_quantity=True)
    return HttpResponse(f'{type(cart.cart)} {cart.get_total_price()} {len(cart)} {cart.cart}')


def change_city(request):
    cart = Cart(request)
    data = request.GET
    shipping_price = 0
    if data['city_id'] != 'NaN':
        shipping_price = AvailableCity.objects.get(id=data['city_id']).shipping_price
    cart_total = cart.get_total_price()
    return JsonResponse({'shippingPrice': shipping_price, 'orderTotal': cart_total + shipping_price})


def add_to_cart(request):
    cart = Cart(request)
    data = request.GET
    product = Product.objects.get(slug=data['product_slug'])
    if 'quantity' in data:
        quantity = data['quantity']
        cart.add(product=product, quantity=quantity, update_quantity=True)
        return HttpResponse(reverse('shop'))

    if str(product.id) not in cart.cart:
        cart.add(product=product, quantity=1, update_quantity=True)

    return HttpResponse(reverse('cart'))


def remove_from_cart(request):
    cart = Cart(request)
    data = request.GET
    product = Product.objects.get(title=data['product_title'])
    total_product_price = cart.get_product_total_price(product)
    cart.remove(product)
    return JsonResponse({'totalProductPrice': total_product_price, 'cartLength': len(cart)})
