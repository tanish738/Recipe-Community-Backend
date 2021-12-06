from django.contrib import admin
from main.models import *
# Register your models here.


admin.site.register(Recipe)

@admin.register(Ingredients)
class IngredientsModelAdmin(admin.ModelAdmin):
    list_display=('ingredient_id','ingredient_name')

# @admin.register(Category)
# class CategoryModelAdmin(admin.ModelAdmin):
#     list_display=('category_id','category_name')



@admin.register(Faqs)
class FAQsModelAdmin(admin.ModelAdmin):
    list_display=('question_id','question')
