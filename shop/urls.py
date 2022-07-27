from django.urls import path
from .views import ShopListView, ProductDetailView

urlpatterns = [
    path('', ShopListView.as_view(), name='shop'),
    path('product/<slug:product_slug>/', ProductDetailView.as_view(), name='product'),
]