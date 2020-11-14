from sites.models import Sites
from rest_framework import viewsets
from .serializers import SiteSerializers

#Sites Viewset
class SitesViewSet(viewsets.ModelViewSet):
    queryset = Sites.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SiteSerializers