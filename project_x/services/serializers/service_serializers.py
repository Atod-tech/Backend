from rest_framework import serializers
from . import Services


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ("name", "description", "active")


# class ArtisanServiceSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = ArtisanService
#         fields = ("artisan", "service")