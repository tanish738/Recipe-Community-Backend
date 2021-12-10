from rest_framework import serializers
from .models import MyUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.exceptions import AuthenticationFailed

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=['email','username','first_name','last_name','profile_picture','is_chef','bio']



class RegistrationSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(style = {'input_type': 'password'}, write_only = True)
    class Meta:
        model = MyUser
        fields = ['email','username','first_name','last_name','profile_picture','password']
        extra_kwargs = {
            'password' : {'write_only' : True},
        }

    def validate(self,attrs):
        username = attrs.get('username',' ')
        if not username.isalnum():
            raise serializers.ValidationError({'username': 'Username must be ALPANUMERIC only!'})
        return attrs
    
    def save(self):
        self.validated_data['is_active'] = False
        my_user = MyUser.objects.create_user(**self.validated_data)
        return my_user

class loginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    class Meta:
        model = MyUser
        fields = ['email', 'password']
        
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        return {'email': user.email}