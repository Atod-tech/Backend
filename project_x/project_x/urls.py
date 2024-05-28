from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from main.views.user_auth import SignUpUserView, SignInUserView

router = routers.DefaultRouter()

router.register("signup/user", SignUpUserView, basename='signup-user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    
    path('signin/client', SignInUserView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
