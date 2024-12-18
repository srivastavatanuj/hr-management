from django.db import models
from employee.models import Employee
from datetime import datetime

# Create your models here.
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendance")
    date = models.DateField(default=datetime.now().date())  
    status = models.PositiveIntegerField(choices=[(0,'Absent'),(1,"First-Half Working"),(2,'Leave'),(3,"Second-Half Working"),(4,'Work From Home'),(5,'Working Office')],default=0) # Indicates if the employee is on leave
    ip=models.CharField(max_length=15,default="00.00.00.00")
    attempt=models.PositiveIntegerField(default=1)

    class Meta:
        unique_together=('employee','date',)


    def __str__(self):
        return f"{self.employee.full_name} - {self.date} ({self.get_status_display()})"
