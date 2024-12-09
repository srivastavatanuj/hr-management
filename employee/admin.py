from django.contrib import admin
from .models import (
    Employee, 
    EmployeeBasicDetails, 
    EmployeeEducationDetails, 
    EmployeeFamilyDetails, 
    EmployeeKYCDetails, 
    EmployeePastWorkExperienceDetails
)

# Register your models here.
admin.site.register(Employee)
admin.site.register(EmployeeBasicDetails)
admin.site.register(EmployeeEducationDetails)
admin.site.register(EmployeeFamilyDetails)
admin.site.register(EmployeeKYCDetails)
admin.site.register(EmployeePastWorkExperienceDetails)
