from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import AttendanceSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class AttendanceView(CreateAPIView):
    serializer_class=AttendanceSerializer
    permission_classes=[IsAuthenticated]