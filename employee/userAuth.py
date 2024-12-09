from django.contrib.auth.base_user import BaseUserManager

class CustomAuthManager(BaseUserManager):
    def create_user(self,email=None,password=None,**extra_fields):
        if not email:
            raise ValueError("Email is required")
        
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,email=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,password=password,**extra_fields)