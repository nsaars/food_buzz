from django.views.generic import CreateView
from home.utils import DataMixin

from contact.forms import ContactMessageForm
from contact.models import ContactMessage


class ContactPageView(DataMixin, CreateView):
    form_class = ContactMessageForm
    model = ContactMessage
    template_name = 'contact/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(self.get_page_context() | context)
