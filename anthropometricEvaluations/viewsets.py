from rest_framework.viewsets import ModelViewSet
from .models import AnthropometricEvaluation
from .serializers import AnthropometricEvaluationSerializer

class AnthropometricEvaluationViewSet(ModelViewSet):
    queryset = AnthropometricEvaluation.objects.all()
    serializer_class = AnthropometricEvaluationSerializer
