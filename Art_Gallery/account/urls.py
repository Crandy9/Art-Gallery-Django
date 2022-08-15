from django.urls import path

from . import views
from .views import *

urlpatterns = [
    # calls registration/login/logout pages
    path('register',views.register, name='register'),
    # login
    path('login', views.login, name='login'),
    # logout
    path('logout', views.logout, name='logout'),
    # my account page accounts/myaccount
    # path('myaccount/<int:pk>', views.myaccount, name='myaccount')
    path('myaccount/<int:pk>', views.userAccount, name='myaccount')
]