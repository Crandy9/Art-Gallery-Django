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
from account.models import Account
from django.contrib import messages
from django.utils.translation import gettext as _
from account.forms import *
from django.http import HttpResponseRedirect

def index(request, pk=None):
    print("Homepage language:" + get_language())
    # dynamically access and fetch Portrait data from db or admin actions
    paintingObjects = Portrait.objects.all()

    if pk is not None:
        #pass Account data 
        account = Account.objects.get(user_id=pk)
        context = {
            'paintingObjects': paintingObjects,
            'account': account
        }
    else:
        # returns <QuerySet [<Portrait: NEW TEST>, <Portrait: TEST 2>]>
        context = {
            'paintingObjects': paintingObjects,
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

# used to redirect to account form if user didn't enter shipping address info
from urllib.parse import urlencode
from urllib.parse import quote as urlquote
from django.urls import reverse
from account.views import userAccount
# also using login_required decorator
@login_required(login_url='/account/login')
def checkout(request, pk=None):
    # uri of account page
    account_uri= reverse(userAccount, kwargs={'pk':request.user.account.user_id})

    # GET
    # if user hasn't updated or entered account info, redirect to account page with message
    if request.user.account.address_entered == False:
        # Please update your shipping address before continuing with your purchase.
        messages.info(request, _('購入を続行する前に、配送先住所を更新してください。'))

        # I need url to look like this: 
        # /ja or en/account/myaccount/pk?next=/ja/checkout/pk
        uri = f'{account_uri}?next={request.path}'
        return redirect(uri)
    # else render the checkout template
    return render(request, 'checkout.html')
