from rest_framework.viewsets import ModelViewSet
from .models import PersonalInformation
from .serializers import PersonalInformationSerializer

class PersonalInformationViewSet(ModelViewSet):
    queryset = PersonalInformation.objects.all()
    serializer_class = PersonalInformationSerializer
