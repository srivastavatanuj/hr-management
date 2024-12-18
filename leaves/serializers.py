from rest_framework import serializers
from .models import EmpLeaveBalance, ApplyLeaves

# Leave Balance Serializer
class LeaveBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpLeaveBalance  # Replace with your LeaveBalance model
        fields = '__all__'

# Apply Leave Serializer
class ApplyLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyLeaves  # Replace with your LeaveApplication model
        fields = ['id', 'employee', 'leave_type', 'start_date', 'end_date', 'reason']

# Leave Status Serializer
class LeaveStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyLeaves
        fields = ['id', 'employee', 'status', 'approval_date', 'comments']

# Applied Leave Serializer
class AppliedLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyLeaves
        fields = ['id', 'employee', 'leave_type', 'start_date', 'end_date', 'status', 'reason']
