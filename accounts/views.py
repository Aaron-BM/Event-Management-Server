from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import  RefreshToken
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework import status
import json
from .models import CustomUser

# LoginView using JWT.
class CustomTokenObtainPairView(TokenObtainPairView):
  serializer_class = CustomTokenObtainPairSerializer


class RegisterView(APIView):

  def post(self, request):
    serializer = RegisterSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': "User registered successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# LogoutView -> blacklisting refresh token
class BlackListRefreshView(APIView):
  def post(self, request):
    try:
      refresh_token = request.data['refresh']
      token = RefreshToken(refresh_token)
      token.blacklist()
      return Response({"success": "Refresh Token Blacklisted Successfully"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
      return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": str(e)})

class isUserDuplicate(APIView):
  def get(self, request, username):
    try:
      user = CustomUser.objects.get(username=username)
      if (user is not None):
        return Response({'userFound': True}, status=status.HTTP_200_OK)
    except CustomUser.DoesNotExist:
      return Response({'userFound': False}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
      return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": str(e)})
    
