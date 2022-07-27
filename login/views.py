from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy

from home.models import Page
from home.utils import DataMixin

from login.forms import LoginUserForm


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login/login.html'

    def get_success_url(self):
        return reverse_lazy('cart')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(self.get_page_context() | context)


def logout_view(request):
    logout(request)
    return redirect('login')
