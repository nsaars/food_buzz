from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from home.utils import DataMixin

from register.forms import RegisterUserForm


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('cart')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(self.get_page_context() | context)