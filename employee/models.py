from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser
from django.db import models
from .userAuth import CustomAuthManager
import uuid



# Create your models here.

class Employee(AbstractBaseUser,PermissionsMixin):
    id = models.CharField(max_length=50, unique=True,primary_key=True)
    full_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_hr=models.BooleanField(default=False)
    is_manager=models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name", "phone"]

    objects=CustomAuthManager()

    def __str__(self):
        return self.full_name

class EmployeeBasicDetails(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="basic_details")
    designation = models.CharField(max_length=100)
    skills=models.CharField(max_length=500)
    phone=models.CharField(max_length=15,unique=True)
    location = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.employee.full_name} - {self.employee.id}"

class EmployeeKYCDetails(models.Model):
    DOCUMENT_TYPES = [
        ("PAN", "PAN Card"),
        ("AADHAR", "Aadhar Card"),
        ("PASSPORT", "Passport"),
        ("DL", "Driving License"),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="kyc_details")
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    document_pdf = models.FileField(upload_to="kyc_documents/")

    def __str__(self):
        return f"{self.employee.full_name} - {self.document_type}"

class EmployeeFamilyDetails(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="family_details")
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    permanent_address = models.TextField()
    personal_email = models.EmailField()
    emergency_contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.employee.full_name} - Family Details"

class EmployeeEducationDetails(models.Model):
    EDUCATION_TYPES = [
        ("UG", "Undergraduate"),
        ("PG", "Postgraduate"),
        ("PHD", "Doctorate"),
        ("DIPLOMA", "Diploma"),
        ("OTHER", "Other"),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="education_details")
    type = models.CharField(max_length=20, choices=EDUCATION_TYPES)
    institute = models.CharField(max_length=150)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    year_of_passing = models.IntegerField()
    certificate = models.FileField(upload_to="education_certificates/")

    def __str__(self):
        return f"{self.employee.full_name} - {self.type}"

class EmployeePastWorkExperienceDetails(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="past_work_experiences")
    company = models.CharField(max_length=150)
    designation = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    reason = models.TextField()
    certificate = models.FileField(upload_to="work_experience_certificates/", null=True, blank=True)

    def __str__(self):
        return f"{self.employee.full_name} - {self.company}"

