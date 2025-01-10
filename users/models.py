from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    is_email_verified = models.BooleanField(default=False)
    otp_created_at = models.DateTimeField(blank=True, null=True) 
    is_developer = models.BooleanField(default=False) 
    email_otp = models.CharField(max_length=6, null=True, blank=True)

    # Override related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Change related_name to avoid conflict
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Change related_name to avoid conflict
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=255, null=False)
    organization_address = models.CharField(max_length=255, null=False)
    organization_website = models.URLField(null=True, blank=True)  # This remains optional
    city = models.CharField(max_length=100, null=True)
    woreda = models.CharField(max_length=100, null=True)
    zone = models.CharField(max_length=100, null=True, blank=True)
    sub_city = models.CharField(max_length=100, null=True, blank=True)
    business_registration_number = models.CharField(max_length=100, null=False)
    STATUS_CHOICES = [ ('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'),] 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
