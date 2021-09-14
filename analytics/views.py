from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.http.response import Http404

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .email import send_activation_email

from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterApiView(generics.CreateAPIView):
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            name = request.data['username']
            email =  request.data['email']
            send_activation_email(name,email)
            user_data = serializer.data
            response = {
                "data": {
                    "user": dict(user_data),
                    "status": "success",
                    "message": "user added successfully please check your email to activate your account",
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class UserProfileApiView(APIView):
    serializer_class = UserSerializer

    def get(self, request, format=None):
        user = request.user
        serializers = UserSerializer(user, many=False)
        return Response(serializers.data)


class ActivateUserApiView(APIView):
  def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except:
            return Http404

  def get(self, request, username, format=None):
    user=self.get_user(username)
    serializers=ActivateSerializer(user)
    return Response(serializers.data)

  # update user to a valid user
  def patch(self, request, username, format=None):
    user=self.get_user(username=username)
    serializers=ActivateSerializer(user, request.data, partial=True)
    if serializers.is_valid(raise_exception=True):
      serializers.save(is_active=True)
      valid_user=serializers.data 

      return Response(valid_user)
    return Response(status.errors, status=status.HTTP_400_BAD_REQUEST)