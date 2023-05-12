from django.db import models
from personalInformations.models import PersonalInformation

class Patient(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=100, blank=True, default='')
    phoneNumber = models.CharField(max_length=100, blank=True, default='')
    personalInformations = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE, blank=True, null=True)

class Meta:
    ordering = ['created_at']