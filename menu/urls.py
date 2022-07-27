from django.urls import path
from .views import MenuPageView

urlpatterns = [
    path('', MenuPageView.as_view(), name='menu')
]