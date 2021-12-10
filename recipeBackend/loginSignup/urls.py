from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns=[
    path('register/',views.reqistration_view, name = "reqistration-view"),
    path('login/',views.login, name = "login"),
    path('all-users/',views.myUsers, name = "retrieve all users"),
    path('email-verify/',views.verifyEmail, name = "verifyEmail"),
]