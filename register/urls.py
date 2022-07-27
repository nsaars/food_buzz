from django.urls import path

from register.views import RegisterUser

urlpatterns = [
    path('', RegisterUser.as_view(), name='register')
]