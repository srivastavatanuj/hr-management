from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView

from .serializers import MarkAttendanceSerializer,AttendanceStatusSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Attendance
from django.db.models import Q
from datetime import date

# Create your views here.
class AttendanceView(CreateAPIView):
    serializer_class=MarkAttendanceSerializer
    permission_classes=[IsAuthenticated]

class EmployeePresentView(ListAPIView):
    serializer_class=AttendanceStatusSerializer
    permission_classes=[AllowAny]
    
    def get_queryset(self):
        return Attendance.objects.filter(Q(date=date.today()) & ~Q(status__in=['leave', 'abs']))

class EmployeeAbsentView(ListAPIView):
    serializer_class=AttendanceStatusSerializer
    permission_classes=[AllowAny]

    def get_queryset(self):
        return Attendance.objects.filter(Q(date=date.today()) & (Q(status='leave') | Q(status='abs')))

class EmployeeStatusView(ListAPIView):
    serializer_class=AttendanceStatusSerializer
    permission_classes=[AllowAny]
    def get_queryset(self):
        return Attendance.objects.filter(Q(employee=self.request.user) & (Q(status='leave') | Q(status='abs')))
