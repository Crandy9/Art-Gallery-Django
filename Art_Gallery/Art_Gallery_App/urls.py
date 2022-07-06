from django.shortcuts import redirect
from django.urls import include, path
# import icon modules
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    # calls index function in views.py
    path('',views.index, name='index'),
    # calls getPortraitData function in views.py
    # path('getPortraitData', views.getPortraitData, name='getPortraitData')

]