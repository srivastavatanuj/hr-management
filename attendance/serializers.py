from random import choices
from rest_framework import serializers
from .models import Attendance

class MarkAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields=('employee','date','status',)


class DailyStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields=('employee','status',)
    
class MonthInputSerializer(serializers.Serializer):
    MONTH_CHOICES = [
        (1, "January"),
        (2, "February"),
        (3, "March"),
        (4, "April"),
        (5, "May"),
        (6, "June"),
        (7, "July"),
        (8, "August"),
        (9, "September"),
        (10, "October"),
        (11, "November"),
        (12, "December"),
    ]
    
    month = serializers.ChoiceField(choices=MONTH_CHOICES)

    class Meta:
        model=Attendance
        fields=('month',)

class EmployeeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields=('date','employee','status',)