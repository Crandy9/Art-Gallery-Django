from django.shortcuts import render, redirect
# for translating between english and japanese
from django.utils.translation import gettext as _
# get_language identifies the language, activate activaes langauges, 
# gettext gets string to be translated
from django.utils.translation import get_language
# to push POST data into database you need to use a model
# messages is used for displaying error messages on html page
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.conf import settings
# accounts app views
from django.contrib.auth.decorators import login_required
# import AccountForm
from account.forms import *
from .models import Account
from phonenumber_field.modelfields import PhoneNumberField
# used for sending emails on account creation
from django.core.mail import send_mail, EmailMessage
# converts html template to a string message for emails
from django.template.loader import render_to_string
# import success messsage
from django.contrib.messages.views import SuccessMessageMixin




# only authenticated and authoritzed users can request this page
# render AccountForm here
@login_required(login_url='login')
def userAccount(request, pk=None):
    # get user form
    user_form = UserForm(request.POST if request.POST else None, instance=request.user)
    # get account form
    account_form = AccountForm(request.POST if request.POST else None, instance = Account.objects.get(user=request.user))

    if request.method == 'POST':
        print('\n')
        print("ACCOUNT FORM IS VALID: " + str(account_form.is_valid()))
        print('\n')
        print("USER FORM IS VALID: " + str(user_form.is_valid()))
        print('\n')

        # first check if form is valid
        if account_form.is_valid() and user_form.is_valid():
            user_form.save()
            account_form.save()
            # set address_entered flag to true so user can make purchases
            account_user = Account.objects.get(user=request.user)
            account_user.address_entered = True
            account_user.save()
            # send success message
            # Your account changes have been saved!
            context = {
                'account_form': account_form,
                'user_form': user_form,
            }

            # send notice when user makes a change to account
            # changed_account_notice template
            # name is the context dictionary used to get the correct user name for email
            template = render_to_string('../templates/changed_account_notice.html', {'name':request.user.first_name})
            email = EmailMessage(
                # email subject title default is 'subject'
                'アカウント情報変更のお知らせ-- There was a change to your account',
                # email template default is 'body'
                template,
                # this will be changed to Kaoru's new gmail 
                settings.EMAIL_HOST_USER,
                # recipient list
                [request.user.email],
            )
            email.fail_silently=False
            # enable this after testing
            email.send()
            
            # check if next param was in url for redirection
            if 'next' in request.POST:
                #  this should be the checkout url
                return redirect(request.POST.get('next'))
            # else just display the form again with success msg
            else:
                # set success message
                messages.success(request, _('変更が正常に保存されました'))
                return render(request,'myaccount.html',context)

        # if form is not valid, redisplay form with error msgs
        else:
            context = {
                'account_form': account_form,
                'user_form': user_form,
            }
            return render(request,'myaccount.html',context)
    context = {
        'account_form': account_form,
        'user_form': user_form,
    }    
    return render(request, 'myaccount.html',context)  

# create register.html in template dir
# CREATING NEW USERS
# param is http request
def register(request):

    # executed when request is post
    # retrieve user entered data
    if request.method == 'POST':
        # http POST is used to fetch data from user
        # and enter it into the db
        # ensure POST string is the same name as the field
        # in register.html file
        if len(request.POST['first_name']) == 0:
            # send error message to page
            messages.info(request,_('名を入力してください'))
            # return to the register page again
            return redirect('register')
        else:
            first_name = request.POST['first_name']
        
        if len(request.POST['last_name']) == 0:
            # send error message to page
            messages.info(request,_('姓を入力してください'))
            # return to the register page again
            return redirect('register')
        else:
            last_name = request.POST['last_name']

        if len(request.POST['username']) == 0:
            # send error message to page
            messages.info(request,_('ユーザー名を入力してください'))
            # return to the register page again
            return redirect('register')
        else:
            username = request.POST['username']

        # need to validate email other than just length
        if len(request.POST['email']) == 0:
            # send error message to page
            messages.info(request,_('有効なメールアドレスを入力してください'))
            # return to the register page again
            return redirect('register')
        else:
            email = request.POST['email']

        if len(request.POST['password1']) == 0:
            # send error message to page
            messages.info(request,_('パスワードを入力して下さい'))
            # return to the register page again
            return redirect('register')
        else:
            password1 = request.POST['password1']

        if len(request.POST['password2']) == 0:
            # send error message to page
            messages.info(request, _('パスワードを再入力してください'))
            # return to the register page again
            return redirect('register')
        else:
            password2 = request.POST['password2']

        # before adding the user, verify passwords match, username is not taken, and email is not registered
        if password1 == password2:
            # next check if the username is not taken
            if User.objects.filter(username=username).exists():
                # send error message to page using existing django messages module
                # https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
                messages.info(request, _('ユーザー名は既に存在します。別のユーザー名を入力してください'))
                # return to the register page again
                return redirect('register')
            # if email is alrady registered
            elif User.objects.filter(email=email).exists():
                # send error message to page
                messages.info(request, _('メールアドレスは既に登録されています。別のメールアドレスを入力してください'))
                # return to the register page again
                return redirect('register')
            else:
                # create a new user for each object instance
                # all of these params are available in the model object that Django provides
                # need to validate email
                user = User.objects.create_user(
                    username = username, 
                    password = password1, 
                    email = email, 
                    first_name = first_name, 
                    last_name = last_name
                )

                # save the user to the db, refresh table, then view again in pgadmin
                user.save()
                # also create and save user account
                user_account = Account.objects.create(
                    user=user,
                )
                user_account.save()

                # send thank you email to new user
                # register_success_email template
                # name is the context dictionary used to get the correct user name for email
                template = render_to_string('../templates/register_success_email.html', {'name':user.first_name})
                email = EmailMessage(
                    # email subject title default is 'subject'
                    'ご登録ありがとうございます！-- Thank you for registering!',
                    # email template default is 'body'
                    template,
                    # this will be changed to Kaoru's new gmail 
                    settings.EMAIL_HOST_USER,
                    # recipient list
                    [user.email],
                )
                email.fail_silently=False
                email.send()
        # passwords do not match
        else:
            messages.info(request,_('パスワードが一致していません。一致するパスワードを再入力してください'))
            # return to the register page again
            return redirect('register')


        # redirect to login page to verify that registration worked
        # and prompt user to login
        messages.info(request, _('アカウントが作成されました！ログインしてください'))
        return redirect('login')


    # executed when http request is get to display the register page
    else:
        return render(request, 'register.html')

# login def
def login(request):
    # fetch user login data
    if request.method == 'POST':
        # get login data
        #username
        if len(request.POST['username']) == 0:
            # send error message to page
            messages.info(request,_('ユーザー名を入力してください'))
            # return to the login page again
            return redirect('login')
        else:
            username = request.POST['username']

        if len(request.POST['password']) == 0:
            messages.info(request, _('入力したパスワードが正しくありません。もう一度お試しください'))
            return redirect('login')
        else:
            #password
            password = request.POST['password']
        # check if username/password is in the db 
        # (later extend functionality to allow email to be entered in lieu of username)
        # use Django's auth module to check user-entered login credentials against db
        # returns user object if the same username and password exists in db, else returns None (null, does not exist)
        user = auth.authenticate(username=username, password=password)

        # if user exists in db
        if user is not None:
            # log the user in, creates a sessionid cookie
            auth.login(request, user)
            key = user.pk
            # redirect to home or other redirection
            # check if next param was in url for redirection
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
        # else if username is not in db
        else:
            messages.error(request, _('このユーザーは存在しません'))
            return redirect('login')

# else if request is GET, go to login page
    else:
        return render(request, 'login.html')

# logout
def logout(request):
    # removes cookie from browser
    auth.logout(request)
    # return to homepage
    return redirect('/')