from rest_framework import serializers
from .models import PersonalInformation

class PersonalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        fields = ['id', 'created_at', 'updated_at', 'dateBirth', 'maritalStatus', 'IntestinalTransit', 'escalaBristol', 'sleepQuality', 'Weight', 'height', 'UrinaryStaining', 'genre', 'profession', 'clinicalHistory', 'objective']
