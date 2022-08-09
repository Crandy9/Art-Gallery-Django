"""Main Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

#internationalization tools
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

# main url mapping. All apps need to have their urls.py urls mapped here
urlpatterns = [
    # allows language choice to be persistent, see index.html post
     path('i18n/', include('django.conf.urls.i18n')),
    ]

# concatenates language suffix to url based on language choice
# to decide which url the homepage initially redirects to, change language in browser settings
urlpatterns += i18n_patterns (
    path('', include('Art_Gallery_App.urls')),
    path('admin/', admin.site.urls), 
    path('account/', include('account.urls')),
    prefix_default_language=True
)
# adding path
urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)