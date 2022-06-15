from django.urls import path

from . import views

# urls.py file copied from calc app

urlpatterns = [
    # calls registration/login/logout pages
    path('register',views.register, name='register'),
    # login
    path('login', views.login, name='login'),
    # logout
    path('logout', views.logout, name='logout')
]