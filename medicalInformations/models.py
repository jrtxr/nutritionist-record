from django.db import models
from patients.models import Patient

class Restriction(models.Model):
    AllergyOrIntolerance = models.CharField(max_length=50, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')

class MedicationUse(models.Model):
    drug = models.CharField(max_length=50, blank=True, default='')
    dose = models.CharField(max_length=50, blank=True, default='')
    schedule = models.TimeField(blank=True, default='')

class Schedules(models.Model):
    wakeUp = models.TimeField(blank=True, default='')
    sleeps = models.TimeField(blank=True, default='')
    physicalActivity = models.TimeField(blank=True, default='')
    
class Condiction(models.Model):
    condiction = models.CharField(max_length=50, blank=True, default='')

class AlterationDigestiveSystem(models.Model):
    alteration = models.CharField(max_length=50, blank=True, default='')

class Diet(models.Model):
    schedule = models.CharField(max_length=50, blank=True, default='')
    food = models.CharField(max_length=50, blank=True, default='')
    quantity = models.CharField(max_length=50, blank=True, default='')

class MedicalInformation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    weightChanges = models.IntegerField(blank=True)
    physicalExam =  models.ManyToManyField(Condiction)
    obsPhysicalExam = models.TextField(max_length=50, blank=True, default='')
    alterationDisgestiveSystem = models.ManyToManyField(AlterationDigestiveSystem)
    obsDisgestiveSystem = models.TextField(max_length=50, blank=True, default='')
    intestinalChanges = models.CharField(max_length=50, blank=True, default='')
    obsIntestinalChanges = models.TextField(blank=True, default='')
    waterConsumption = models.CharField(max_length=50, blank=True, default='') 
    restrictions = models.ForeignKey(Restriction, on_delete=models.CASCADE)
    useOfMedicines = models.ManyToManyField(MedicationUse)
    alcoholicBeverage = models.CharField(max_length=50, blank=True, default='')
    smoking = models.CharField(max_length=50, blank=True, default='')
    schedules = models.ForeignKey(Schedules, on_delete=models.CASCADE)
    physicalActivityDescription = models.CharField(max_length=100, blank=True, default='')
    dietEvaluation = models.ForeignKey(Diet, on_delete=models.CASCADE)
    foodPreferences = models.TextField(blank=True, default='')
    foodAversions = models.TextField(blank=True, default='')
    inappetence = models.TextField(blank=True, default='')
    hyperphagia = models.TextField(blank=True, default='')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)

class Meta:
    ordering = ['created_at']
