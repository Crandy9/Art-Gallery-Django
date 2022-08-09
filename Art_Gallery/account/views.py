from django.shortcuts import render, redirect
# for translating between english and japanese
from django.utils.translation import gettext as _
# get_language identifies the language, activate activaes langauges, 
# gettext gets string to be translated
from django.utils.translation import get_language, activate, gettext
# to push POST data into database you need to use a model
# django provides user models and auth models
# messages is used for displaying error messages on html page
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.core.mail import send_mail
# accounts app views
from django.contrib.auth.decorators import login_required


# only authenticated and authoritzed users can request this page
@login_required(login_url='login')
def myaccount(request, pk=None):

    # if user is logged in
    if request.user.is_authenticated:
        # log the user in, creates a sessionid cookie
        return render(request,'myaccount.html')
    # make a default error message and redirect to homepage
    else:
        return redirect('login')

    
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
                user = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name, last_name = last_name)

                # save the user to the db, refresh table, then view again in pgadmin
                user.save()
                # send error message to page

        # passwords do not match
        else:
            messages.info(request,_('パスワードが一致していません。一致するパスワードを再入力してください'))
            print("Register error language:" + get_language())
            # return to the register page again
            return redirect('register')
        print("Register redirect to login language:" + get_language())

        # SEND EMAIL TEST
        subject = 'TIIIAAAANNNNKKK.'
        message = "It's haaapaa. ANd I told ya. Cause I know ya. And you know that"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email,]
        send_mail(subject,message,email_from,recipient_list)

        # redirect to login page to verify that registration worked
        # and prompt user to login
        return redirect('login')


    # executed when http request is get to display the register page
    else:
        print("Reegister get language:" + get_language())
        return render(request, 'register.html')

# login def
def login(request):
    # fetch user login data
    if request.method == 'POST':
        print("Login POST language:" + get_language())
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
            # redirect to home
            return redirect('/')
        # else if username is not in db
        else:
            messages.error(request, _('このユーザーは存在しません'))
            return redirect('login')

# else if request is GET, go to login page
    else:
        print("Login GET language:" + get_language())
        return render(request, 'login.html')

# logout
def logout(request):
    print("log out language:" + get_language())
    # removes cookie from browser
    auth.logout(request)
    # return to homepage
    return redirect('/')