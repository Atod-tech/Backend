from rest_framework.viewsets import ModelViewSet
from . import (
    ServiceSerializers, 
    # ArtisanServiceSerializers, 
    ArtisanProfile, 
    # ArtisanService
    Services
    )


class ServiceTypeViewSet(ModelViewSet):
    queryset = Services.objects.select_related("artisan", "service")
    serializer_class = ServiceSerializers