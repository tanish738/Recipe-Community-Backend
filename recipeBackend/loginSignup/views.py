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

#for token 
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

#Mail
from django.core.mail import send_mail

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

def emailauth(request,pk):
    context={"pk":pk}
    if request.method=="POST":
        for token in Token.objects.all():
            if str(token)==pk:
                token.delete()
                Token.objects.create(user=token.user)
                #return redirect('login page url frontend')
        
    return render(request,"email.html",context)


@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        token=Token.objects.create(user = instance)
        subject="Recipe Community"
        url="http://127.0.0.1:8000/login-signup/token/"+str(token)+"/"
        message = "Thank you for logging in Recipe Community please verify your email."+url
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email, ]
        send_mail( subject, message, email_from, recipient_list )
