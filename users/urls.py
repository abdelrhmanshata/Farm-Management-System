from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ProfileView,UpdateUserView

# Add URL pattern for user registration
# Add URL pattern for user login using JWT token obtain pair view
# Add URL pattern for refreshing JWT token
# Add URL pattern for accessing user profile
# Add URL pattern for update user profile
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path('update/', UpdateUserView.as_view(), name='update-user'),
]
