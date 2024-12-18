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
        fields=('email','password')

    
class ChangePasswordSerializer(serializers.Serializer):
    old_password=serializers.CharField(required=True)
    new_password=serializers.CharField(required=True)

    class Meta:
        model=Employee
        fields=('old_password','new_password')

    def validate(self, attrs):
        user=self.context['request'].user
        if not user.check_password(attrs['old_password']):
            raise serializers.ValidationError({"error":"invalid password"})
        attrs.pop('old_password')
        return attrs

    def save(self, **kwargs):
        user=self.context['request'].user
        new_password=self.validated_data['new_password']
        user.set_password(new_password)
        user.save()
        return user

class ManageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('full_name','email')
