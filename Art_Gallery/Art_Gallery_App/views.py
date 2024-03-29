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
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage


EMAIL_ON = True

def index(request, pk=None):
    print("\nHomepage language:" + get_language() + '\n')
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


    # if user hasn't updated or entered account info, redirect to account page with message
    if request.user.account.address_entered == False:
        # get URL of account page
        # userAccount is the view name, and kwargs is the account's user_id which is the user's pk
        account_uri= reverse(userAccount, kwargs={'pk':request.user.account.user_id})
        # Please update your shipping address before continuing with your purchase.
        messages.info(request, _('購入を続行する前に、配送先住所を更新してください。'))

        # I need url to look like this: 
        # /ja or en/account/myaccount/pk?next=/ja/checkout/pk
        uri = f'{account_uri}?next={request.path}'
        return redirect(uri)
    # else render the checkout template
    # get the object's id
    product = Portrait.objects.get(pk=pk)
    # check if the product isn't already sold: in case a user comes to this page somehow
    if product.is_sold is True:
        messages.warning(request, _('このアイテムは利用できません。'))
        return redirect('/')
    # get user's country to charge correct currency
    currentUser = request.user
    # get total cost for usd
    usdShippingHandling = product.usa_shipping_price
    usdPrice = product.dollar_price
    usdTotal = usdShippingHandling + usdPrice
    print("USD TOTAL: " + str(usdTotal) + '\n')
    context = {
        'currentUser': currentUser,
        'product':product,
        'usdTotal': usdTotal,

    }
    return render(request, 'checkout.html', context)


# thankyou page showing successful payment details
# show thankyou message
# purchase summary:
# painting name
# amount paid
# order number (This number will be used to confirm your purchase in the event we need to contact you regarding your shipment, )
# expected delivery date
# set this painting's isSold field to true

# pk is portrait id
@login_required
def thankyou(request, pk=None):
    
    # get specific image
    purchasedPainting = Portrait.objects.get(pk=pk)
    # check if the product isn't already sold: in case a user comes to this page somehow
    if purchasedPainting.is_sold is True:
        messages.warning(request, _('このアイテムは利用できません。'))
        return redirect('/')
    # set this image's isSold field to True
    purchasedPainting.is_sold = True
    # save it
    purchasedPainting.save()
    # get current user
    currentUser = request.user
    # get painting uuid and converting it to string
    uuid = str(purchasedPainting.uuid)
    print("Painting's uuid: " + str(uuid) + '\n')
    # only give last 12 chars to user to be used for order number
    orderId = uuid[-8:]
    print("OrderId: " + str(orderId) + '\n')


    # send thankyou email
    # get country-specific email
    if currentUser.account.country == 'JP':
        # total cost
        jpy_total = purchasedPainting.price + purchasedPainting.japan_shipping_price
        template = render_to_string('../templates/japan_thankyou_email.html',
        {'name':request.user.first_name,
         'japanese_painting_name': purchasedPainting.name,
         'english_painting_name': purchasedPainting.english_name,
         'orderId':orderId,
         'jpy_price':purchasedPainting.price,
         'jpy_shipping_price': purchasedPainting.japan_shipping_price,
         'jpy_total_price_paid': jpy_total,
         })
        email = EmailMessage(
            # email subject title default is 'subject'
            'ご購入いただきありがとうございます！ -- Thank you for your purchase!',
            # email template default is 'body'
            template,
            # this will be changed to Kaoru's new gmail 
            settings.EMAIL_HOST_USER,
            # recipient list
            [request.user.email],
        )
        email.fail_silently=False
        # only send email if this flag is true
        if EMAIL_ON:
            email.send()
        
            context = {
                'jpy_total': jpy_total, 
                'currentUser': currentUser,
                'purchasedPainting': purchasedPainting,
                'orderId': orderId
            }
            print("jpy total: " + str(jpy_total) + '\n')
    else:
        # total cost
        usd_total = purchasedPainting.dollar_price + purchasedPainting.usa_shipping_price
        template = render_to_string('../templates/usa_thankyou_email.html',
        {'name':request.user.first_name,
         'japanese_painting_name': purchasedPainting.name,
         'english_painting_name': purchasedPainting.english_name,
         'orderId':orderId,
         'usd_price':purchasedPainting.dollar_price,
         'usd_shipping_price': purchasedPainting.usa_shipping_price,
         'usd_total_price_paid': usd_total,
         })

        email = EmailMessage(
            # email subject title default is 'subject'
            'ご購入いただきありがとうございます！ -- Thank you for your purchase!',
            # email template default is 'body'
            template,
            # this will be changed to Kaoru's new gmail 
            settings.EMAIL_HOST_USER,
            # recipient list
            [request.user.email],
        )
        email.fail_silently=False
        # only send email if this flag is true
        if EMAIL_ON:
            email.send()
            context = {
                'usd_total': usd_total, 
                'currentUser': currentUser,
                'purchasedPainting': purchasedPainting,
                'orderId': orderId
            }
            print("usd total: " + str(usd_total) + '\n')

    return render(request, 'thankyou.html', context)


# handle 404s, 500 server errors, 
def error(request, exception):
    return render(request,'error.html')

