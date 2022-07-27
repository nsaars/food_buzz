from datetime import datetime

from django.views.generic import TemplateView

from reservation.forms import ReservationForm
from shop.models import Product, Category
from .models import TodaySpecialProduct
from .utils import DataMixin


class HomePageView(DataMixin, TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['special_products'] = TodaySpecialProduct.objects.filter(date=datetime.today())
        if not context['special_products']:
            previous_special_date = TodaySpecialProduct.objects.filter(date__lte=datetime.today()).first().date
            context['special_products'] = TodaySpecialProduct.objects.filter(date=previous_special_date)

        products_by_category = {}
        categories = Category.objects.all()
        for category in categories:
            products_by_category[category] = Product.objects.filter(category=category)
        context['products_by_category'] = products_by_category.items()

        context['form'] = ReservationForm
        return dict(self.get_page_context() | context)
