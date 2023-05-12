from rest_framework import serializers
from .models import AnthropometricEvaluation

class AnthropometricEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnthropometricEvaluation
        fields = ['id', 'created_at', 'updated_at', 'PhysicalActivityLevel', 'currentWeight', 'Circumferenceabdominal', 'Circumferencewaist', 'Circumferencearm', 'Circumferencecalf', 'Circumferencehip', 'SkinfoldBiceps', 'SkinfoldTriceps', 'SkinfoldSubscapular', 'SkinfoldMediumAxillary', 'SkinfoldSuprailiac', 'SkinfoldSupraspinal', 'SkinfoldAbdominal' , 'SkinfoldThigh', 'SkinfoldCalf', 'SkinfoldBreastplate']
