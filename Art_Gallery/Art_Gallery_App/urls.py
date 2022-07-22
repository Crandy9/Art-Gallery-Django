from django.shortcuts import redirect
from django.urls import include, path, re_path
# import icon modules
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    # calls index function in views.py
    # sends the pk
    path('', views.index, name='index'),
    path('carousel/<int:pk>', views.carousel, name='carousel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)