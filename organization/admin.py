from django.contrib import admin
from .models import Organization,Holiday,NoticeBoard,LeavePolicy

# Register your models here.
admin.site.register(Organization)
admin.site.register(Holiday)
admin.site.register(NoticeBoard)
admin.site.register(LeavePolicy)