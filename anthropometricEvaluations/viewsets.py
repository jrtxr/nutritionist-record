from rest_framework.viewsets import ModelViewSet
from anthropometricEvaluations.models import AnthropometricEvaluation
from anthropometricEvaluations.serializers import AnthropometricEvaluationSerializer

class PersonalInformationViewSet(ModelViewSet):
    queryset = AnthropometricEvaluation.objects.all()
    serializer_class = AnthropometricEvaluationSerializer
