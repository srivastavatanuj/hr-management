from django.db import models

# Create your models here.
class Organization(models.Model):
    # basic details
    name=models.CharField(max_length=255)
    domain=models.CharField(max_length=100,unique=True)
    registration_number=models.CharField(max_length=50,unique=True,blank=True,primary_key=True)
    logo=models.ImageField(upload_to="org_logos",blank=True,null=True)
    industry_type=models.CharField(max_length=100)
    website=models.CharField(max_length=100,unique=True,blank=True)
    contact_email=models.EmailField()
    contact_phone=models.CharField(max_length=20)
    date_created=models.DateField(auto_now_add=True)

    # admin details
    
    # is_active=models.BooleanField(default=True)
    # subscription_plan=models.CharField(max_length=50,choices=[('basic','basic'),('pro','pro'),('enterprise','enterprise')],default='basic')



class LeavePolicy(models.Model):
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE,related_name='leaves')
    leave_type = models.CharField(max_length=50, choices=[
        ('sick', 'Sick Leave'),
        ('casual', 'Casual Leave'),
        ('paid', 'Paid Leave'),
        ('maternity', 'Maternity Leave'),
        ('flexi', 'Flexi Leave'),
    ])
    max_days=models.PositiveIntegerField()
    carry_forward=models.BooleanField(default=False)
    applicable_from=models.DateField()
    applicable_to=models.DateField()
    leaves_per_month=models.FloatField()

class Holiday(models.Model):
    org=models.ForeignKey(Organization,on_delete=models.CASCADE,related_name='holiday')
    name=models.CharField(max_length=100)
    date=models.DateField()
    flexi=models.BooleanField(default=False)

class NoticeBoard(models.Model):
    org=models.ForeignKey(Organization,on_delete=models.CASCADE,related_name='notice')
    subject=models.CharField(max_length=500)
    description=models.TextField()
    time=models.DateTimeField(auto_now=True)
    priority=models.CharField(max_length=100,choices=[('low','low'),('mid','mid'),('high','high')])