from django import forms

from reservation.models import Reservation
from reservation.widgets import TimePickerInput, DatePickerInput


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Full Name*"}),
            'phone_number': forms.TextInput(attrs={'placeholder': "Phone Number*"}),
            'email': forms.EmailInput(attrs={'placeholder': "Your Email"}),
            'table_size': forms.Select(attrs={'class': 'res-tab table-zone'}),
            'time': TimePickerInput(attrs={'data-provide': "timepicker"}),
            'date': DatePickerInput(attrs={'data-provide': "datepicker"}),
            'comment': forms.Textarea(attrs={'rows': "6", 'placeholder': "Message"}),
        }
