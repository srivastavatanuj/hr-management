from rest_framework import serializers
from .models import Attendance

class MarkAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields=('status',)

class AttendanceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields=('employee','status',)
