from django.urls import path

from . import views

urlpatterns = [
    # calls registration/login/logout pages
    path('register',views.register, name='register'),
    # login
    path('login', views.login, name='login'),
    # logout
    path('logout', views.logout, name='logout'),
    # my account page accounts/myaccount
    path('myaccount', views.myaccount, name='myaccount')
]