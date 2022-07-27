from django.views.generic import TemplateView

from shop.models import Category, Product
from home.utils import DataMixin


class MenuPageView(DataMixin, TemplateView):
    template_name = "menu/menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products_by_category = {}
        categories = Category.objects.order_by('menu_order').all()
        for category in categories:
            products_by_category[category] = Product.objects.filter(category=category)
        context['products_by_category'] = products_by_category.items()
        return dict(self.get_page_context() | context)
