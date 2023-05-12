from rest_framework.viewsets import ModelViewSet
from .models import AnthropometricEvaluation
from .serializers import AnthropometricEvaluationSerializer

class PersonalInformationViewSet(ModelViewSet):
    queryset = AnthropometricEvaluation.objects.all()
    serializer_class = AnthropometricEvaluationSerializer
