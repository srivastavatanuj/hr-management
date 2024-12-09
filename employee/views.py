from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenRefreshSerializer

from .serializers import LoginSerializer, ManageSerializer, ResetPasswordSerializer, SignupSerializer
# Create your views here.

class LoginView(TokenObtainPairSerializer):
    pass

# class LoginView(CreateAPIView):
#     serializer_class=LoginSerializer
#     permission_classes=[AllowAny]

class SignupView(CreateAPIView):
    serializer_class=SignupSerializer
    permission_classes=[AllowAny]

class ResetView(CreateAPIView):
    serializer_class=ResetPasswordSerializer
    permission_classes=[AllowAny]

class ManageEmployee(CreateAPIView):
    serializer_class=ManageSerializer
    permission_classes=[AllowAny,IsAuthenticated]