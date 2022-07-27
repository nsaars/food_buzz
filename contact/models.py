from django.db import models
from django.urls import reverse_lazy


class ContactMessage(models.Model):
    name = models.CharField(max_length=31, null=False)
    email = models.EmailField(max_length=63, null=False)
    subject = models.CharField(max_length=63, null=False)
    message = models.TextField(null=False)

    def get_absolute_url(self):
        return reverse_lazy('contact')