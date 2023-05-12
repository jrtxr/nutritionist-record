from rest_framework.viewsets import ModelViewSet
from .models import MedicalInformation
from .serializers import MedicalInformationSerializer

class MedicalInformationViewSet(ModelViewSet):
    queryset = MedicalInformation.objects.all()
    serializer_class = MedicalInformationSerializer
