from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
#MODELS
from .models import MyUser

#LOGIN
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import update_last_login
#SERIALIZERS
from .serializers import MyUserSerializer, RegistrationSerializer,loginSerializer

#FOR API VIEW & REST_FRAMEWORK
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

#TOKEN 
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

#Mail
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from .utils import Util
# Create your views here.

#on get request it returns all users 
#password is not encrypted
@api_view(['POST',])
@permission_classes(())
def reqistration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            my_user = serializer.save()
            token = Token.objects.get(user = my_user).key
            # email verification
            current_site = get_current_site(request).domain
            relative_link = reverse('verifyEmail')
            absurl = 'http://' + current_site + relative_link + "?token="+str(token)
            email_body = 'Hi' + my_user.username + 'Use link below to verify your email \n' + absurl
            data_email = {'email_body': email_body, 'to_email': my_user.email, 'email_subject':'Verify your email'}
            Util.send_email(data_email)
        else:
            data = serializer.errors
        return Response(data)


@api_view(['GET'])
@permission_classes(())
def verifyEmail(request): #what to do if user clicks on link again as now the token has been reset, put a quick fix by try and except
    data = {}
    token = request.GET.get('token')
    try:
        user = MyUser.objects.get(auth_token = token)
    except:
        content = {'detail': 'User already activated!'}
        return Response(content, status = status.HTTP_200_OK)
    data['response'] = "successfully registered a new user"
    data['username'] = user.username
    data['email'] = user.email
    data['token'] = token
    if user.is_active == False:
        user.is_active = True
        user.save()
        Token.objects.get(user = user).delete()
        Token.objects.create(user = user)
        new_token = Token.objects.get(user = user).key
        data['new_token'] = new_token
        return Response(data, status = status.HTTP_200_OK)
    return Response(data, status = status.HTTP_200_OK)

@api_view(['POST',])
@permission_classes(())
def login(request):
    if request.method == 'POST':
        serializer = loginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = MyUser.objects.get(email = serializer.data['email'])
        token = Token.objects.get(user = user).key
        update_last_login(None, user) #update last login
        data = {}
        data['email'] = user.email
        data['token'] = token
        return Response(data, status = status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAdminUser,]) 
def myUsers(request):
    myUsers = MyUser.objects.all()
    serializer = MyUserSerializer(myUsers, many = True)
    return Response(serializer.data)

