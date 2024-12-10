from django.db import models
from employee.models import Employee

# Create your models here.
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendance")
    date = models.DateField(auto_now_add=True)  
    status = models.CharField(max_length=100,choices=[('wfo','Working Office'),('wfh','Work From Home'),('leave','Leave'),('abs','Absent'),('fhw',"First-Half Working"),('shw',"Second-Half Working")],default='abs') # Indicates if the employee is on leave


    class Meta:
        unique_together = ('employee', 'date',)

    def __str__(self):
        return f"{self.employee.full_name} - {self.date} ({self.status})"
