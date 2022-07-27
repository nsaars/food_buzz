from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse_lazy


class Reservation(models.Model):
    table_sizes = (
        ("Table Size", "Table Size"),
        ("2F - 3F", "2F - 3F"),
        ("2.5F - 3.5F", "2.5F - 3.5F"),
        ("3F - 4F", "3F - 4F"),
        ("3.5F - 4.5F", "3.5F - 4.5F"),
        ("5F - 6F", "5F - 6F"),
        ("5.5F - 6.5", "5.5F - 6.5F")
    )
    name = models.CharField(max_length=63)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    email = models.EmailField(max_length=127, blank=True, null=True)
    table_size = models.CharField(max_length=31, choices=table_sizes, default="Table Size", null=True)
    time = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy('reservation')