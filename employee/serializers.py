from rest_framework import serializers
from .models import Employee

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('uuid','email','password')

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('full_name','email','phone')

class ResetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('email',)

class ManageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('full_name','email','phone')
