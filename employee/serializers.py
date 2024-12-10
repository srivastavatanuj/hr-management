import re
from typing import Required
from rest_framework import serializers
from .models import Employee

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('id','email','password')

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('id','full_name','email')

class ResetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('email',)
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password=serializers.CharField(required=True)
    new_password=serializers.CharField(required=True)

    class Meta:
        model=Employee
        fields=('old_password','new_password')

    def save(self, **kwargs):
        import pdb
        pdb.set_trace()
        return super().save(**kwargs)

class ManageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('full_name','email')
