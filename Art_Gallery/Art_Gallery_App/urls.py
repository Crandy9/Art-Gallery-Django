from django.shortcuts import redirect
from django.urls import include, path
# import icon modules
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from . import views

# urls.py file copied from calc app

urlpatterns = [
    # calls index function in views.py
    path('',views.index, name='index'),
    # adding redirect for icons
    path("favicon.ico",
    RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")))

]