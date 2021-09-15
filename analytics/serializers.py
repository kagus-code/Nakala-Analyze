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


class SignUpSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username','email','password']
    extra_kwargs = {
      "password": {'write_only': True}
    }

  def create(self, validated_data):
          password =validated_data.pop('password', None)
          instance =self.Meta.model(**validated_data)
          if password is not None:
             instance.set_password(password)
          instance.is_active=False
          instance.save()   
          return instance

class ActivateSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['is_active']      


class UploadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Csv
    fields = ['file_name']      