from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns=[
    path('recipe/',views.RecipeApi.as_view()),
    path('ingredients/',views.IngredientsApi.as_view()),
    path('faqs/',views.FAQsApi.as_view()),
]