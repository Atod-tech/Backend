from main.models import User, ArtisanProfile
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import re

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields = ("id", "first_name", "last_name", "email", "contact", "password")
    
    def create(self, validated_data):
        # Extract password from validated_data
        password = validated_data.pop("password", None)
        if password:
            # Validate the password using regular expressions
            if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).+$', password):
                raise ValidationError(
                    {"error": "Passwords must include at least one special symbol, one number, one lowercase letter, and one uppercase letter."})


        user = User.objects.create(**validated_data)
        # Confirm the user as a store owner
        if password:
            # Set and save the user's password only if a valid password is provided
            user.set_password(password)
            user.save()
        return user
    
    
class ArtisanProfileSerializer(ModelSerializer):
    class Meta:
        model = ArtisanProfile
        fields = "__all__"
        
    def create(self, validated_data):
        user = validated_data.pop("user")
        
        user = request 


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
