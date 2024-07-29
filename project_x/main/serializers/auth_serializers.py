from main.models import User, ArtisanProfile
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404, Http404
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "contact", "password")

    def create(self, validated_data):
        # Extract password from validated_data
        password = validated_data.pop("password", None)
        address = validated_data.get("address")
        longitude = validated_data.get("longitude")
        latitude = validated_data.get("latitude")
        business_contact = validated_data.get("business_contact")
        service_type = validated_data.get("service_type")
        years_of_experience = validated_data.get("years_of_experience")
        
        if password:
            # Validate the password using regular expressions
            if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).+$', password):
                raise ValidationError(
                    {"error": "Passwords must include at least one special symbol, one number, one lowercase letter, and one uppercase letter."})

        instance = User.objects.create(**validated_data)
        
        if validated_data.get("is_professional", False):
            artisan= ArtisanProfile.objects.create(
                user=instance, 
                address=address, 
                longitude=longitude, 
                latitude=latitude, 
                business_contact=business_contact, 
                service_type=service_type,
                years_of_experience=years_of_experience
            )
            artisan.save()
        if password:
            # Set and save the user's password only if a valid password is provided
            instance.set_password(password)
            instance.save()
        return instance
    
    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        artisan_profiles = ArtisanProfile.objects.filter(user=instance)
        representation["artisan"] = ArtisanProfileSerializer(artisan_profiles, many=True).data
        return representation



class ArtisanProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtisanProfile
        fields = "__all__"
        
    def to_representation(self, instance):
        representation = super(ArtisanProfileSerializer, self).to_representation(instance)
        representation["service_type"] = [service.name for service in instance.service_type.all()]
        return representation


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        contact = attrs.get("contact")
        password = attrs.get("password")

        user = authenticate(request=self.context.get("request"), contact=contact, password=password)

        if not user:
            raise AuthenticationFailed(
                'No active account found with the given credentials'
            )
        return super().validate(attrs)