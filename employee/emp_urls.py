from django.urls import path
from .views import ManageEmployee,ListEmployeeView,ListAdminView


urlpatterns = [
  path('list-employees/',ListEmployeeView.as_view(),name='reset'),
  path('list-admins/',ListAdminView.as_view(),name='reset'),
  path('manage/<int:pk>/',ManageEmployee.as_view(),name='manage'),
]
