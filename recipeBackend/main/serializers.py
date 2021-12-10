from rest_framework import serializers
from .models import *
"""
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
"""


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    #recipe_ingredients=IngredientsSerializer(many=False,read_only=True)
    class Meta:
        model = Recipe
        fields ="__all__"

    




class FaqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faqs
        fields = '__all__'