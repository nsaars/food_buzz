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

        context['special_products_with_image'] = TodaySpecialProduct.get_today_special_products_with_images()

        context['products_with_image_by_category'] = Category.get_products_with_image_by_category()

        context['form'] = ReservationForm
        return dict(self.get_page_context() | context)
