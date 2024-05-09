from .models import Provider
from rest_framework.viewsets import ModelViewSet
from .serializers import ProviderSerializer
from .permissions import IsStaff


class ProviderViewSet(ModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
