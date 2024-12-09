from django.db import models
from employee.models import Employee


class EmpLeaveBalance(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="leave_balance")
    sick = models.IntegerField(default=0)
    casual = models.IntegerField(default=0)
    paid = models.IntegerField(default=0)
    maternity = models.IntegerField(default=0)
    flexi = models.IntegerField(default=0)

    def __str__(self):
        return f"Leave Balance for {self.employee.full_name}"


# Leave Application Model
class ApplyLeaves(models.Model):
    LEAVE_TYPE_CHOICES = [
        ("SICK", "Sick Leave"),
        ("CASUAL", "Casual Leave"),
        ("PAID", "Paid Leave"),
        ("MATERNITY", "Maternity Leave"),
        ("FLEXI", "Flexible Leave"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="applied_leaves")
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    approved_by_manager = models.BooleanField(default=False)
    approved_by_hr = models.BooleanField(default=False)

    def __str__(self):
        return f"Leave Application by {self.employee.full_name} ({self.status})"