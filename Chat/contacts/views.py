from rest_framework.viewsets import ModelViewSet
from .api.serializers import ContactsSerializer, Contacts
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissions
# Create your views here.


class ContactsViewSet(ModelViewSet):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    authentication_classes = (SessionAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    # Sobrescribir los métodos
