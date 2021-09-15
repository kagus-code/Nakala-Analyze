from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime
from rest_framework.serializers import Serializer

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
            user = User.objects.get(username=name)
            id = user.id
            send_activation_email(name,email,id)
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
  # update user to a valid user
  def patch(self, request, id, format=None):
    user=User.objects.get(id=id)
    serializers=ActivateSerializer(user, request.data, partial=True)
    if serializers.is_valid(raise_exception=True):
      serializers.save(is_active=True)
      valid_user=serializers.data 
      response = {
                "data": {
                    "user": dict(valid_user),
                    "status": "success",
                    "message": "Your email has been successfully confirmed you can now log in",
                }
            }
      return Response(response, status=status.HTTP_200_OK)
    return Response(status.errors, status=status.HTTP_400_BAD_REQUEST)



class UploadDataApiView(generics.CreateAPIView):
    serializer_class=UploadSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            obj = Csv.objects.get(activated=False)
            with open(obj.file_name.path, 'r',encoding='latin1') as f:
                insert_count = CovidData.objects.from_csv(
                    f,
                    delimiter=",", 
                    drop_constraints=True, 
                    drop_indexes=True, 
                    encoding="latin-1",
                    ignore_conflicts=True
                    )
                print(f"{insert_count} records inserted")
                Csv.objects.filter(activated=False).update(activated=True)
                response = {
                "data": {
                    "status": "success",
                    "message": (f"{insert_count} records inserted"),
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)




class CovidDataAPIView(APIView):
    def get(self, request, format=None):
        all_data = CovidData.objects.all()
        serializers = CovidDataSerializer(all_data, many=True)
        return Response(serializers.data)




class CovidDataAPIView(APIView):
    def get_data(self, pk):
        try:
            return CovidData.objects.get(pk=pk)
        except CovidData.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        covid_data = self.get_data(pk)
        serializers = CovidDataSerializer(covid_data)
        return Response(serializers.data)


class CovidDataByIsoAPIView(APIView):
    serializer_class = CovidDataSerializer
    def get(self,request,iso,format=None):
        data = CovidData.objects.filter(iso_code=iso)
        serializers=self.serializer_class(data, many=True)
        return Response(serializers.data)



