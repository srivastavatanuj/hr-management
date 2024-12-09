from django.db import models

# Create your models here.
class Contact(models.Model):
    SUBJECT_CHOICES = [
        ("GENERAL", "General Inquiry"),
        ("SUPPORT", "Support Request"),
        ("FEEDBACK", "Feedback"),
        ("OTHER", "Other"),
    ]

    name = models.CharField(max_length=100)  # Name of the person contacting
    email = models.EmailField()  # Email of the person contacting
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)  # Subject with predefined choices
    description = models.TextField()  # Detailed message or description
    dateTime = models.DateTimeField(auto_now_add=True)  # Automatically sets to the time the contact is created

    def __str__(self):
        return f"{self.name} - {self.get_subject_display()}"
