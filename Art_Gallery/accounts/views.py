from django.shortcuts import render, redirect

# to push POST data into database you need to use a model
# django provides user models and auth models
# messages is used for displaying error messages on html page
from django.contrib import messages
from django.contrib.auth.models import User, auth
# accounts app views

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
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # before adding the user, verify passwords match, username is not taken, and email is not registered
        if password1 == password2:
            # next check if the username is not taken
            if User.objects.filter(username=username).exists():
                # send error message to page using existing django messages module
                # https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
                messages.info(request, 'Username already exists')
                # return to the register page again
                return redirect('register')
            # if email is alrady registered
            elif User.objects.filter(email=email).exists():
                # send error message to page
                messages.info(request,'Email is already registered')
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
            messages.info(request,'passwords do not match')
            # return to the register page again
            return redirect('register')

 

        # redirect to login page to verify that registration worked
        # and prompt user to login
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
        username = request.POST['username']
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
            messages.error(request, 'username or password is incorrect')
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