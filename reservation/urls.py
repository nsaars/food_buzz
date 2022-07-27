from django.urls import path
from .views import ReservationPageView
urlpatterns = [
    path('', ReservationPageView.as_view(), name='reservation')
]