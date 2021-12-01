from django.contrib import admin
from main.models import *
# Register your models here.
@admin.register(Recipe)
class RecipeModelAdmin(admin.ModelAdmin):
    list_display=('recipe_id','recipe_name','owned_by')
    list_filter=('recipe_category','recipe_ingredients')

@admin.register(Ingredients)
class IngredientsModelAdmin(admin.ModelAdmin):
    list_display=('ingredient_id','ingredient_name')

# @admin.register(Category)
# class CategoryModelAdmin(admin.ModelAdmin):
#     list_display=('category_id','category_name')

@admin.register(Region)
class RegionModelAdmin(admin.ModelAdmin):
    list_display=('region_id','region_name')

@admin.register(Faqs)
class FAQsModelAdmin(admin.ModelAdmin):
    list_display=('question_id','question')