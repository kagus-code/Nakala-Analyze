from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken






class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['id',  'username', 'email','is_active']



class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)