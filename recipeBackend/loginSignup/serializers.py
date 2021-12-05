from rest_framework import serializers
from .models import *


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=['email','username','first_name','last_name','profile_picture','is_chef','bio','password']