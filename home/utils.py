from django.urls import resolve

from home.models import Page


class DataMixin:
    def get_page_context(self, **kwargs):
        context = kwargs
        context['pages'] = Page.objects.filter(show=True)
        context['title'] = resolve(self.request.path).url_name
        return context
