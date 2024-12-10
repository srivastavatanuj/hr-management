from django.urls import path
from .views import SignupView,ResetView,ManageEmployee,ListEmployeeView,ListAdminView,ChangePasswordView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  path('login/',TokenObtainPairView.as_view(),name='login'),
  path('signup/',SignupView.as_view(),name='signup'),
  path('reset/',ResetView.as_view(),name='reset'),
  path('change-password/',ChangePasswordView.as_view(),name='reset'),
  path('list-employees/',ListEmployeeView.as_view(),name='reset'),
  path('list-admins/',ListAdminView.as_view(),name='reset'),
  path('manage/<int:pk>/',ManageEmployee.as_view(),name='manage'),
]
