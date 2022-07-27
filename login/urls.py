from django.urls import path
from .views import LoginUser, logout_view

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('logout/', logout_view, name='logout')
]
