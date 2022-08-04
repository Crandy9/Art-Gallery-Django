from django.shortcuts import redirect
from django.urls import include, path, re_path
# import icon modules
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf.urls.static import static
from django.conf import settings
from . import views
#internationalization tools
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    # calls index function in views.py
    path('', views.index, name='index'),
    # by default, URL looks like this: /ja/carousel/14
    path('carousel/<int:pk>', views.carousel, name='carousel'),
    path('checkout/<int:pk>', views.checkout, name='checkout')
]


urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)