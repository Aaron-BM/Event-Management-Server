from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)
  
    token["role"] = user.role
    token["full_name"] = user.full_name

    return token
  
  def validate(self, attrs):
    data = super().validate(attrs)

    data.update({
      'id': self.user.id,
      'username': self.user.username,
      'email': self.user.email,
      'full_name': self.user.full_name,
      'role': self.user.role,
    })

    return data
  

class RegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)
  class Meta:
    model = CustomUser
    fields = ['username', 'full_name', 'email', 'password', 'role', 'contact']
  def create(self, validated_data):
    user = CustomUser.objects.create_user(
      username=validated_data['username'],
      email=validated_data['email'],
      full_name=validated_data['full_name'],
      password=validated_data['password'],
      role=validated_data['role'],
      contact=validated_data['contact'],
    )

    return user
  
