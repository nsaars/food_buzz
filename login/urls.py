from django.urls import path
from .views import LoginUser

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
]
