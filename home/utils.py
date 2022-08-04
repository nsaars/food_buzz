from django.urls import resolve, reverse


class Page:
    def __init__(self, title, slug):
        self.__title = title
        self.__slug = slug

    def get_absolute_url(self):
        return reverse(self.__slug)

    @property
    def title(self):
        return self.__title


class DataMixin:
    def get_page_context(self, **kwargs):
        context = kwargs
        slugs = ['home', 'menu', 'reservation', 'shop', 'contact', 'cart',
                 'logout' if self.request.user.is_authenticated else 'login']
        pages = [Page(slug.title(), slug) for slug in slugs]
        context['pages'] = pages
        context['title'] = resolve(self.request.path).url_name
        return context
