from rest_framework import serializers

from .models import *




class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'


class FaqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faqs
        fields = '__all__'