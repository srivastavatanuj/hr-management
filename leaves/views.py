from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import EmpLeaveBalance, ApplyLeaves
from .serializers import (
    LeaveBalanceSerializer,
    ApplyLeaveSerializer,
    LeaveStatusSerializer,
    AppliedLeaveSerializer,
)

# Leave Balance View
class LeaveBalanceView(ListAPIView):
    queryset = EmpLeaveBalance.objects.all()
    serializer_class = LeaveBalanceSerializer

# Apply Leave View
class ApplyLeaveView(CreateAPIView):
    queryset = ApplyLeaves.objects.all()
    serializer_class = ApplyLeaveSerializer

# Leave Status List View
class LeaveStatusListView(ListAPIView):
    queryset = ApplyLeaves.objects.all()
    serializer_class = LeaveStatusSerializer

# Leave Status Detail View
class LeaveStatusDetailView(RetrieveAPIView):
    queryset = ApplyLeaves.objects.all()
    serializer_class = LeaveStatusSerializer
    lookup_field = 'id'

# All Applied Leaves View
class AllAppliedLeavesView(ListAPIView):
    queryset = ApplyLeaves.objects.all()
    serializer_class = AppliedLeaveSerializer

# Applied Leave Detail View
class AppliedLeaveDetailView(RetrieveAPIView):
    queryset = ApplyLeaves.objects.all()
    serializer_class = AppliedLeaveSerializer
    lookup_field = 'id'
