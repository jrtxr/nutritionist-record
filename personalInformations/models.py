from django.db import models

class PersonalInformation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dateBirth = models.DateTimeField(max_length=100, blank=True)
    maritalStatus = models.CharField(max_length=50, blank=True, default='')
    IntestinalTransit = models.CharField(max_length=50, blank=True, default='')
    escalaBristol = models.IntegerField(blank=True)
    sleepQuality = models.CharField(max_length=100, blank=True, default='')
    Weight = models.FloatField(blank=True)
    height = models.FloatField(blank=True)
    UrinaryStaining = models.IntegerField(blank=True)
    genre = models.CharField(max_length=20, blank=True, default='')
    profession = models.CharField(max_length=50, blank=True, default='')
    clinicalHistory = models.TextField(max_length=100, blank=True, default='')
    objective = models.TextField(max_length=100, blank=True, default='')

class Meta:
    ordering = ['created_at']
