from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns=[
    path('register/',views.RegisterApi.as_view()),
    path('login/',views.CustomLogin.as_view()),
]