from django.urls import path
from .views import *

urlpatterns = [
    path('balance/', LeaveBalanceView.as_view(), name='leave-balance'),
    path('apply/', ApplyLeaveView.as_view(), name='apply-leave'),
    path('status/', LeaveStatusListView.as_view(), name='leave-status'),
    path('status/<int:id>/', LeaveStatusDetailView.as_view(), name='leave-status-detail'),
    path('all-applied-leaves/', AllAppliedLeavesView.as_view(), name='all-applied-leaves'),
    path('all-applied-leaves/<int:id>/', AppliedLeaveDetailView.as_view(), name='applied-leave-detail'),
]
