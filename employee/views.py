from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenRefreshSerializer
from django.utils.crypto import get_random_string
from rest_framework.exceptions import NotFound

from .permissions import isAdmin

from .models import Employee
from django.db.models import Q
from .serializers import LoginSerializer, ManageSerializer, ResetPasswordSerializer, SignupSerializer,ChangePasswordSerializer
# Create your views here.


class SignupView(CreateAPIView):
    serializer_class=SignupSerializer
    permission_classes=[IsAuthenticated,isAdmin]

    def perform_create(self, serializer):
        password=get_random_string(12)
        print(password)
        user=serializer.save()
        user.set_password(password)
        user.save()


class ResetView(UpdateAPIView):
    serializer_class=ResetPasswordSerializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        email=self.request.data.get('email')
        try:
           return Employee.objects.get(email=email)
        except Employee.DoesNotExist:
            raise NotFound("User Not Found")

    def perform_update(self, serializer):
        newPassword=get_random_string(12)
        user=serializer.save()
        user.set_password(newPassword)
        user.save()


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
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Employee.objects.get(id=user.pk)
    