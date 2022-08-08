from django.views.generic import TemplateView

from shop.models import Category, Product, ProductImage
from home.utils import DataMixin


class MenuPageView(DataMixin, TemplateView):
    template_name = "menu/menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['products_with_image_by_category'] = Category.get_products_with_image_by_category()

        return dict(self.get_page_context() | context)
