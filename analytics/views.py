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
      user_data =serializer.data
      response={
        "data":{
            "user":dict(user_data),
            "status":"success",
            "message":"user added successfully",
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




