from django.contrib import admin

from .models import ApplyLeaves,EmpLeaveBalance

# Register your models here.
admin.site.register(ApplyLeaves)
admin.site.register(EmpLeaveBalance)
