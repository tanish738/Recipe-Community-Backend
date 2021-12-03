from django.shortcuts import render
#MODELS
from .models import MyUser

#SERIALIZERS
from .serializers import MyUserSerializer

#FOR API VIEW & REST_FRAMEWORK
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

#TOKEN 
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

# Create your views here.


class RegisterApi(generics.ListCreateAPIView):
    queryset =MyUser.objects.all()
    serializer_class = MyUserSerializer


class CustomLogin(ObtainAuthToken):
    def get(self, request, *args, **kwargs):
        users=MyUser.objects.all()
        serializer=MyUserSerializer(users,many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        print(serializer)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })