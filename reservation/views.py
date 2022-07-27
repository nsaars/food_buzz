from home.utils import DataMixin
from django.views.generic import CreateView

from reservation.forms import ReservationForm
from reservation.models import Reservation


class ReservationPageView(DataMixin, CreateView):
    form_class = ReservationForm
    model = Reservation
    template_name = 'reservation/reservation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(self.get_page_context() | context)