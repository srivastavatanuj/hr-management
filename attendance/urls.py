from django.urls import path
from .views import AttendanceView,EmployeeAbsentView,EmployeeStatusView,EmployeePresentView

urlpatterns = [
  path('',AttendanceView.as_view(),name="attendance"),
  path('<int:pk>/',EmployeeStatusView.as_view(),name="monthly-status"),
  path('absent/',EmployeeAbsentView.as_view(),name="absent"),
  path('present/',EmployeePresentView.as_view(),name="present"),
]
