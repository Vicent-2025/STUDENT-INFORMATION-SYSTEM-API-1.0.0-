from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import StudentViewSet, RegisterUserView

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # User Registration
    path('register/', RegisterUserView.as_view(), name='register'),

    # Login
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Refresh Token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]