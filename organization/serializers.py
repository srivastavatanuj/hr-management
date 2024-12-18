from rest_framework import serializers
from .models import Holiday, NoticeBoard, LeavePolicy,Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization  # Replace with your actual Holiday model
        fields = '__all__'  # Include all fields; customize if needed

# Holiday Serializer
class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday  # Replace with your actual Holiday model
        fields = '__all__'  # Include all fields; customize if needed

# Notice Board Serializer
class NoticeBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeBoard  # Replace with your actual NoticeBoard model
        fields = '__all__'

# Leave Policy Serializer
class LeavePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = LeavePolicy  # Replace with your actual LeavePolicy model
        fields = '__all__'
