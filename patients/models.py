from django.db import models

class Patient(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=100, blank=True, default='')
    phoneNumber = models.CharField(max_length=100, blank=True, default='')

class Meta:
    ordering = ['created_at']