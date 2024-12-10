from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView
from rest_framework.permissions import AllowAny

from .serializers import ContactSerializer
from .models import Contact
from employee.permissions import isAdmin

# Create your views here.
class CreateView(CreateAPIView):
    serializer_class=ContactSerializer
    permission_classes=[AllowAny]

class ListQueryView(ListAPIView):
    serializer_class=ContactSerializer
    permission_classes=[isAdmin]

    def get_queryset(self):
        return Contact.objects.all()

class RetrieveQueryView(RetrieveAPIView):
    serializer_class=ContactSerializer
    permission_classes=[isAdmin]

    def get_queryset(self):
        id = self.kwargs['pk']
        return Contact.objects.filter(id=id)