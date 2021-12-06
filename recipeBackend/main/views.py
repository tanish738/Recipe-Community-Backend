from django.shortcuts import render\


#FOR API AND REST_FRAMEWORK
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

#FOR MODELS
from .models import *

#FOR SERILAZERS 
from .serializers import *




# Create your views here.

class RecipeApi(generics.ListCreateAPIView):
    queryset =Recipe.objects.all()
    serializer_class = RecipeSerializer

"""
@api_view(['GET', 'POST'])
def customer_list(request):
    if request.method=="GET":
        customer=Customer.objects.all()
        serializer=CustomerSerializer(customer, many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        data=JSONParser().parse(request)
        serializer=CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
class IngredientsApi(generics.ListCreateAPIView):
    queryset= Ingredients.objects.all()
    serializer_class=IngredientsSerializer


class FAQsApi(generics.ListCreateAPIView):
    queryset=Faqs.objects.all()
    serializer_class=FaqsSerializer


#function to create token for new user



