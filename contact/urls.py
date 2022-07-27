from django.urls import path
from .views import ContactPageView
urlpatterns = [
    path('', ContactPageView.as_view(), name='contact')
]