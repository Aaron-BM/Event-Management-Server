from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView, RegisterView, BlackListRefreshView, isUserDuplicate

urlpatterns = [
    path("auth/login/", CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("auth/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("auth/register/", RegisterView.as_view(), name='register'),
    path("auth/logout/", BlackListRefreshView.as_view(), name='logout'),
    path("user/<str:username>/", isUserDuplicate.as_view(), name='check-username-duplicate')

]
