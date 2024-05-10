from .models import Provider
from rest_framework.viewsets import ModelViewSet
from .serializers import ProviderSerializer
from .permissions import IsStaff


class ProviderViewSet(ModelViewSet):
    """
    API endpoint that allows providers to be viewed or edited.
    """

    serializer_class = ProviderSerializer

    permission_classes = [IsStaff]

    def get_queryset(self):
        """
        All providers or filtering by country
        """
        country = self.request.query_params.get("country")
        if country:
            return Provider.objects.filter(contact__country=country)
        return Provider.objects.all()
