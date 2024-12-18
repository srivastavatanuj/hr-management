
from rest_framework.generics import CreateAPIView,ListAPIView,GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



from .serializers import MarkAttendanceSerializer,DailyStatusSerializer,MonthInputSerializer,EmployeeStatusSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Attendance
from employee.models import Employee
from django.db.models import Q
from datetime import datetime
# from ipware import get_client_ip

from employee.permissions import isAdmin

# Create your views here.
class AttendanceView(APIView):
    serializer_class=MarkAttendanceSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user=self.request.user
        if user.is_manager:
            empId=request.data['employee']
            date=request.data['date']
            attendanceStatus=request.data['status']
            emp = Employee.objects.get(id=empId)
            obj,created = Attendance.objects.get_or_create(employee=emp,date=date)
            if created:
                return Response({"success":"attendance marked by admin"},status=status.HTTP_201_CREATED)
            else:
                obj.date=date
                obj.status=attendanceStatus
                obj.save()
                return Response({"success":"attendance updated by admin"},status=status.HTTP_200_OK)
        else:
            attendanceStatus=request.data['status']
            obj,created = Attendance.objects.get_or_create(employee=user,status=attendanceStatus,date=datetime.now().date())
            if created:
                return Response({"success":"attendance marked"},status=status.HTTP_201_CREATED)
            else:
                return Response({"error":"attendance already marked"},status=status.HTTP_400_BAD_REQUEST)

class EmployeePresentView(ListAPIView):
    serializer_class=DailyStatusSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return Attendance.objects.filter(Q(date=datetime.now().date()) & ~Q(status__in=['leave', 'abs']))

class EmployeeAbsentView(ListAPIView):
    serializer_class=DailyStatusSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Attendance.objects.filter(Q(date=datetime.now().date()) & (Q(status='leave') | Q(status='abs')))

class EmployeeStatusView(GenericAPIView):
    output_serializer_class=EmployeeStatusSerializer
    serializer_class=MonthInputSerializer

    queryset = Attendance.objects.all()

    def post(self, request, *args, **kwargs):
        user=self.request.user
        month=request.data['month']
        queryset = Attendance.objects.filter(employee=user, date__month=month)
        output_serializer=self.output_serializer_class(queryset,many=True)
        return Response(output_serializer.data,status=status.HTTP_200_OK)

class DailyStatusView(GenericAPIView):
    serializer_class=DailyStatusSerializer
    permission_classes=[AllowAny]

    def get(self, request, *args, **kwargs):
        absent=Attendance.objects.filter(Q(date=datetime.now().date()) & (Q(status=0) | Q(status=2)))
        present=Attendance.objects.filter(Q(date=datetime.now().date()) & ~Q(status__in=[0, 2]))
        
        absent_serializer=DailyStatusSerializer(absent)
        absent_serializer=DailyStatusSerializer(absent)

        import pdb
        pdb.set_trace()
        # pending=
        return Response({"present":0,"absent":absent}, status=status.HTTP_200_OK)



###########
# fake data
###########

# from faker import Faker
# from employee.models import Employee

# def add_emp_attendance():
#     fake=Faker()
#     emp = Employee.objects.values_list('id', flat=True)
#     for _ in range(200):
#         randomempid = fake.random_int(min=0,max=len(emp)-1)
#         status=fake.random_int(min=0,max=5)
#         date="2024-12-17"
        
#         employee_instance = Employee.objects.get(id=int(emp[randomempid]))
#         Attendance.objects.create(employee=employee_instance,date=str(date),status=status)
        