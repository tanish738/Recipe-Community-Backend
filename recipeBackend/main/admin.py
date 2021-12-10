from django.contrib import admin
from main.models import *
# Register your models here.


admin.site.register(Recipe)

admin.site.register(Ingredients)

# @admin.register(Category)
# class CategoryModelAdmin(admin.ModelAdmin):
#     list_display=('category_id','category_name')



@admin.register(Faqs)
class FAQsModelAdmin(admin.ModelAdmin):
    list_display=('question_id','question')
