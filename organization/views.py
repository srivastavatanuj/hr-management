from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated

from employee.permissions import isAdmin
from .models import Holiday, NoticeBoard, LeavePolicy, Organization  # Replace with your actual models
from .serializers import HolidaySerializer, NoticeBoardSerializer, LeavePolicySerializer,OrganizationSerializer  # Replace with your serializers

# Holiday Views
class HolidayListView(ListAPIView):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    permission_classes=[IsAuthenticated]

class HolidayCreateView(CreateAPIView):
    serializer_class = HolidaySerializer


class HolidayDetailView(RetrieveAPIView):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    lookup_field = 'id'


# Notice Board Views
class NoticeBoardListView(ListAPIView):
    queryset = NoticeBoard.objects.all()
    serializer_class = NoticeBoardSerializer


class NoticeBoardCreateView(CreateAPIView):
    serializer_class = NoticeBoardSerializer


class NoticeBoardDetailView(RetrieveAPIView):
    queryset = NoticeBoard.objects.all()
    serializer_class = NoticeBoardSerializer
    lookup_field = 'id'


# Leave Policy Views
class LeavePolicyListView(ListAPIView):
    queryset = LeavePolicy.objects.all()
    serializer_class = LeavePolicySerializer


class LeavePolicyCreateView(CreateAPIView):
    serializer_class = LeavePolicySerializer


class LeavePolicyDetailView(RetrieveAPIView):
    queryset = LeavePolicy.objects.all()
    serializer_class = LeavePolicySerializer
    lookup_field = 'id'


# General View and Edit Views
class GeneralAddView(CreateAPIView):
    serializer_class=OrganizationSerializer
    permission_classes=[isAdmin]
    queryset=Organization.objects.all()

class GeneralManageView(ListAPIView):
    serializer_class=OrganizationSerializer
    permission_classes=[AllowAny]
    queryset=Organization.objects.all()


class GeneralEditView(RetrieveUpdateDestroyAPIView):
    serializer_class=OrganizationSerializer
    permission_classes=[AllowAny]

    def get_permissions(self):
        if self.request.method=="POST":
            self.permission_classes=[isAdmin]
        self.permission_classes=[AllowAny]

        return [permission() for permission in self.permission_classes]

    def get_object(self):
        return Organization.objects.all()[0]


    

    
