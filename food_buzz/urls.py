from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from food_buzz import settings
from home import urls as home_urls
from shop import urls as shop_urls
from reservation import urls as reservation_urls
from menu import urls as menu_urls
from contact import urls as contact_urls
from cart import urls as cart_urls
from register import urls as register_urls
from login import urls as login_urls
from login.views import logout_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)),
    path('shop/', include(shop_urls)),
    path('reservation/', include(reservation_urls)),
    path('menu/', include(menu_urls)),
    path('contact/', include(contact_urls)),
    path('cart/', include(cart_urls)),
    path('register/', include(register_urls)),
    path('login/', include(login_urls)),
    path('logout/', logout_view, name='logout')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

