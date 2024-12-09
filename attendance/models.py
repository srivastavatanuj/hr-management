from django.db import models
from employee.models import Employee

# Create your models here.
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendance")
    date = models.DateField()  # Date of the attendance record
    on_leave = models.BooleanField(default=False)  # Indicates if the employee is on leave

    def __str__(self):
        status = "On Leave" if self.on_leave else "Present"
        return f"{self.employee.full_name} - {self.date} ({status})"
