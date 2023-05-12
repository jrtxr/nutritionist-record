from rest_framework.viewsets import ModelViewSet
from patients.models import Patient
from personalInformations.serializer import PersonalInformationSerializer

class PersonalInformationViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PersonalInformationSerializer
