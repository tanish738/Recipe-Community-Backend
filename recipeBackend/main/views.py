from django.http.response import HttpResponse
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

#post_save
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your views here.

#what to do for the ingredients field and model??
class RecipeApi(generics.ListCreateAPIView): #will have to use FBV to set the owned by field diectly by token
    queryset =Recipe.objects.all()
    serializer_class = RecipeSerializer
    def post(self,request):
        serilazer=RecipeSerializer(data=request.data)
        if serilazer.is_valid():
            serilazer.save()
            print(serilazer)
            return Response(serilazer.data, status=status.HTTP_201_CREATED)
        return HttpResponse('Fucked up')
    


@receiver(post_save, sender =Recipe)
def create_recipe(sender,instance = None, created = False, **kwargs):
    if created:
        if(type(instance.recipe_id)==int):
            print("op")
            Ingredients.objects.create(recipe_id=int(instance.recipe_id),ingredient_name=instance.recipe_name)
            print(Ingredients.objects.get(recipe_id=instance.recipe_id))
class ReciepeCreateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Recipe.objects.all()
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

"""
class ExampleView(APIView):

    def get(self, request, format=None):
        content = {
            'recipe': str(Recipe.objects.all()),
        }
        return Response(content)
    def post(self,request,*args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
"""
class ExampleView(APIView):
    def get(self,request):
        user=Recipe.objects.all()
        serilazer=RecipeSerializer(user,many=True)
        return Response(serilazer.data)
    def post(self,request):
        serilazer=RecipeSerializer(data=request.data)
        if serilazer.is_valid():
            serilazer.save()
            print(serilazer)
            return Response(serilazer.data, status=status.HTTP_201_CREATED)
        return(serilazer.errors)
