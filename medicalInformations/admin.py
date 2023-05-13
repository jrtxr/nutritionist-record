from django.contrib import admin
from .models import MedicalInformation, Schedules, Restriction, MedicationUse, Diet, AlterationDigestiveSystem, Condiction
# Register your models here.


admin.site.register(MedicalInformation)
admin.site.register(Schedules)
admin.site.register(Restriction)
admin.site.register(MedicationUse)
admin.site.register(Diet)
admin.site.register(AlterationDigestiveSystem)
admin.site.register(Condiction)
