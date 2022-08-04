from datetime import datetime

from django.views.generic import TemplateView

from reservation.forms import ReservationForm
from shop.models import Product, Category, ProductImage
from .models import TodaySpecialProduct
from .utils import DataMixin


class HomePageView(DataMixin, TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        special_products = TodaySpecialProduct.objects.filter(date=datetime.today())
        if not special_products:
            previous_special = TodaySpecialProduct.objects.filter(date__lte=datetime.today()).first()
            if previous_special:
                previous_special_date = previous_special.date
                special_products = TodaySpecialProduct.objects.filter(date=previous_special_date)
        context['special_products_with_image'] = [(special_product, ProductImage.objects.filter(product=special_product.product).first()) for special_product in special_products]
        products_by_category = {}
        categories = Category.objects.all()
        for category in categories:
            products_by_category[category] = [(product, ProductImage.objects.filter(product=product).first()) for product in Product.objects.filter(category=category)]
        context['products_with_image_by_category'] = products_by_category.items()

        context['form'] = ReservationForm
        return dict(self.get_page_context() | context)
