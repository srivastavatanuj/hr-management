from django.urls import path
from .views import LoginView,SignupView,ResetView,ManageEmployee
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  path('login/',TokenObtainPairView.as_view(),name='login'),
  path('signup/',SignupView.as_view(),name='signup'),
  path('reset/',ResetView.as_view(),name='reset'),
  path('manage/',ManageEmployee.as_view(),name='manage'),
]
