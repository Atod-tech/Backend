from main.models import User
from rest_framework.viewsets import ModelViewSet
from main.serializers.auth_serializers import UserSerializer, TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class SignUpUserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class SignInUserView(TokenObtainPairView):
    # permission_classes = (permissions.AllowAny,)
    serializer_class = TokenObtainPairSerializer