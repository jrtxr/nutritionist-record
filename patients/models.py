from django.db import models
# Create your models here.
class Patient(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=100, blank=True, default='')
    phone_number = models.CharField(max_length=100, blank=True, default='')

class Meta:
    ordering = ['created_at']