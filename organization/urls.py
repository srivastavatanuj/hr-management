from django.urls import include

from django.urls import path, include
from .views import *  # Import your views here

urlpatterns = [
    # Holiday-related URLs
    path('holiday/', HolidayListView.as_view(), name='holiday-list'),
    path('holiday/create/', HolidayCreateView.as_view(), name='holiday-create'),
    path('holiday/<int:id>/', HolidayDetailView.as_view(), name='holiday-detail'),

    # Notice Board-related URLs
    path('notice-board/', NoticeBoardListView.as_view(), name='notice-board-list'),
    path('notice-board/create/', NoticeBoardCreateView.as_view(), name='notice-board-create'),
    path('notice-board/<int:id>/', NoticeBoardDetailView.as_view(), name='notice-board-detail'),

    # Leave Policy-related URLs
    path('leave-policy/', LeavePolicyListView.as_view(), name='leave-policy-list'),
    path('leave-policy/create/', LeavePolicyCreateView.as_view(), name='leave-policy-create'),
    path('leave-policy/<int:id>/', LeavePolicyDetailView.as_view(), name='leave-policy-detail'),

    # General view and edit actions
    path('add/', GeneralAddView.as_view(), name='view'),
    path('view/', GeneralManageView.as_view(), name='view'),
    path('edit/', GeneralEditView.as_view(), name='edit'),
]
