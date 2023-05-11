from django.db import models

# Create your models here.
class Patients(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=100, blank=True, default='')
    phone = models.CharField(max_length=100, blank=True, default='')