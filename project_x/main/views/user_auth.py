from main.models import ArtisanProfile, User
from rest_framework.viewsets import ModelViewSet
from main.serializers.auth_serializers import UserSerializer, TokenObtainPairSerializer, ArtisanProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class SignUpUserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArtisanProfile(ModelViewSet):
    queryset = ArtisanProfile.objects.select_related("user")
    serializer_class = ArtisanProfile


class SignInUserView(TokenObtainPairView):
    # permission_classes = (permissions.AllowAny,)
    serializer_class = TokenObtainPairSerializer