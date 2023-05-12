from rest_framework import serializers
from .models import MedicalInformation

class MedicalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInformation
        fields = ['id', 'created_at', 'updated_at', 'weightChanges', 'weightChanges', 'obsPhysicalExam', 'alterationDisgestiveSystem', 'obsDisgestiveSystem', 'intestinalChanges', 'obsIntestinalChanges', 'waterConsumption', 'restrictions', 'useOfMedicines', 'alcoholicBeverage', 'smoking', 'schedules', 'physicalActivityDescription', 'dietEvaluation', 'foodPreferences', 'foodAversions', 'inappetence', 'hyperphagia']