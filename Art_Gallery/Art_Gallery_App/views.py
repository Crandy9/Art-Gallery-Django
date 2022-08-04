from cgitb import text
from urllib import response
from django.shortcuts import redirect, render
from django.views.generic import View
from .models import *
from django.core import serializers
from django.http import HttpResponse
# for translating between english and japanese
from django.utils.translation import gettext as _
# get_language identifies the language, activate activaes langauges, 
# gettext gets string to be translated
from django.utils.translation import get_language, activate, get_language_from_request
from django.conf import settings
from django.contrib.auth.decorators import login_required

#  put all translations here
def translate(language):
    pass
    # current_lang = get_language()
    # print("\nCURRENT LANGUAGE:" + language + '\n')

    # activate english
    # try:
    #     activate(language)
        # underscore is short for gettext which will try to retrieve the translation
        # of the given strings, if they exist
        # title = _("薫のアートギャラリー")
        # sign_in = _("ログイン")
        # register = _("会員登録")

    # finally:
    #     activate(current_lang)
    # return translations
    # return title, sign_in, register

def index(request, pk=None):
    print("Homepage language:" + get_language())
    # dynamically access and fetch Portrait data from db or admin actions
    paintingObjects = Portrait.objects.all()

    # returns <QuerySet [<Portrait: NEW TEST>, <Portrait: TEST 2>]>
    context = {
        'paintingObjects': paintingObjects
    }


    # display  index.html file in templates folder with data 
    return render(request, "index.html", context)

def carousel(request, pk=None):
    if request.method == 'GET':
        print("Carousel language:" + get_language())

        # get the specific object by its pk
        # exclude empty or null values
        carouselObjects = Portrait.objects.get(pk=pk)

        # return both carousel object and carousel list
        context = {
            'carouselObjects': carouselObjects
        }

        # return the data with the specific object data
        return render(request, "carousel.html", context)

@login_required(login_url='/accounts/login')
def checkout(request, pk=None):
    print("Checkout language:" + get_language())
    return render(request, 'checkout.html', response)