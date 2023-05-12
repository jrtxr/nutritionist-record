from django.db import models
from patients.models import Patient

class AnthropometricEvaluation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    PhysicalActivityLevel = models.FloatField(blank=True)
    currentWeight = models.FloatField(blank=True)

    Circumferenceabdominal = models.FloatField(blank=True)
    Circumferencewaist = models.FloatField(blank=True)
    Circumferencearm = models.FloatField(blank=True)
    Circumferencecalf = models.FloatField(blank=True)
    Circumferencehip = models.FloatField(blank=True)

    SkinfoldBiceps = models.FloatField(blank=True)
    SkinfoldTriceps = models.FloatField(blank=True)
    SkinfoldSubscapular = models.FloatField(blank=True)
    SkinfoldMediumAxillary = models.FloatField(blank=True)
    SkinfoldSuprailiac = models.FloatField(blank=True)
    SkinfoldSupraspinal = models.FloatField(blank=True)
    SkinfoldAbdominal = models.FloatField(blank=True)
    SkinfoldThigh = models.FloatField(blank=True)
    SkinfoldCalf = models.FloatField(blank=True)
    SkinfoldBreastplate = models.FloatField(blank=True)

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)


class Meta:
    ordering = ['created_at']
