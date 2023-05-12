from rest_framework import serializers
from personalInformations.models import PersonalInformation

class AnthropometricEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        fields = ['id', 'created_at', 'updated_at', 'PhysicalActivityLevel', 'currentWeight', 'Circumferenceabdominal', 'Circumferencewaist', 'Circumferencearm', 'Circumferencecalf', 'Circumferencehip', 'SkinfoldBiceps', 'SkinfoldTriceps', 'SkinfoldSubscapular', 'SkinfoldMediumAxillary', 'SkinfoldSuprailiac', 'SkinfoldSupraspinal', 'SkinfoldAbdominal' , 'SkinfoldThigh', 'SkinfoldCalf', 'SkinfoldBreastplate']
