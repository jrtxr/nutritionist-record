from rest_framework.viewsets import ModelViewSet
from personalInformations.models import PersonalInformation
from personalInformations.serializer import PersonalInformationSerializer

class PersonalInformationViewSet(ModelViewSet):
    queryset = PersonalInformation.objects.all()
    serializer_class = PersonalInformationSerializer
