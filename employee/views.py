from telnetlib import STATUS
from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenRefreshSerializer
from django.utils.crypto import get_random_string
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import isAdmin

from .models import Employee
from django.db.models import Q
from .serializers import LoginSerializer, ManageSerializer, ResetPasswordSerializer, SignupSerializer,ChangePasswordSerializer
import uuid
from datetime import datetime


class SignupView(CreateAPIView):
    serializer_class=SignupSerializer
    permission_classes=[IsAuthenticated,isAdmin]

    # def perform_create(self, serializer):
    #     password=get_random_string(12)
    #     print(password)
    #     user=serializer.save()
    #     user.set_password(password)
    #     user.save()
    #     return Response({"password":password},status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = get_random_string(12) 
        user = serializer.save()
        user.set_password(password)
        user.save()

        return Response(
            {
                "message": "User created successfully",
                "password": password,
            },
            status=status.HTTP_201_CREATED,

        )


class ResetView(APIView):
    serializer_class=ResetPasswordSerializer
    permission_classes=[AllowAny]

    def post(self, request, *args, **kwargs):
        email=request.data['email']
        if not Employee.objects.filter(email=email).exists():
            return Response({"error":"Invaid user"},status=status.HTTP_404_NOT_FOUND)
        
        try:
            resetHash=self.kwargs['hash']
            newPassword=request.data['password']
            user=Employee.objects.get(email=email)
            if len(newPassword)<8:
                return Response({"error":"password should be atleast 8 character long"},status=status.HTTP_400_BAD_REQUEST)
            elif user.hash==resetHash and user.timestamp>int(datetime.now().timestamp()):
                user.set_password(newPassword)
                user.save()
                return Response({"success":"password changed successully"},status=status.HTTP_200_OK)
            else:
                return Response({"error":"link expired"},status=status.HTTP_400_BAD_REQUEST)
        except:
            resetHash=uuid.uuid4()
            timestamp=int(datetime.now().timestamp())+15*60
            user=Employee.objects.get(email=email)
            user.hash=resetHash
            user.timestamp=timestamp
            user.save()
            reset_link=request.build_absolute_uri()+f"{resetHash}/"
            print(reset_link)
            return Response({"success":"email sent to your mail","link":reset_link},status=status.HTTP_200_OK)


class ListEmployeeView(ListAPIView):
    serializer_class=SignupSerializer
    permission_classes=[IsAuthenticated,isAdmin]

    def get_queryset(self):
        return Employee.objects.filter(Q(is_manager=False) & Q(is_hr=False))


class ListAdminView(ListAPIView):
    serializer_class=SignupSerializer
    permission_classes=[isAdmin,IsAuthenticated]

    def get_queryset(self):
        return Employee.objects.filter(Q(is_manager=True) | Q(is_hr=True))


class ManageEmployee(RetrieveUpdateDestroyAPIView):
    serializer_class=ManageSerializer
    permission_classes=[IsAuthenticated,isAdmin]

    def get_queryset(self):
    
        id=self.kwargs['pk']
        return Employee.objects.get(id=id)
    

class ChangePasswordView(UpdateAPIView):
    serializer_class=ChangePasswordSerializer
    permission_classes=[AllowAny]


    def get_object(self):
        user=self.request.user
        return Employee.objects.get(id=user.pk)
    

from faker import Faker

def add_emp():
    fake=Faker()
    for _ in range(10):
        id=fake.random_int(min=100000,max=999999)
        name=fake.name()
        email=fake.email()
        print(id,name,email)
        Employee.objects.create(id=id,full_name=name,email=email)
