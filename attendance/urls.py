from django.urls import path

from .views import AttendanceView,EmployeeAbsentView,EmployeeStatusView,EmployeePresentView,DailyStatusView

urlpatterns = [
  path('mark/',AttendanceView.as_view(),name="attendance"),
  path('monthly-status-employee/',EmployeeStatusView.as_view(),name="monthly-status"),
  path('monthly-status-all/',EmployeeStatusView.as_view(),name="monthly-status"),
  path('daily-absent/',EmployeeAbsentView.as_view(),name="absent"),
  path('daily-present/',EmployeePresentView.as_view(),name="present"),
  path('daily-status/',DailyStatusView.as_view(),name="daily"),
]
