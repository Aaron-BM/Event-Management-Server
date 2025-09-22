from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  ROLE_CHOICES = (
    ('user', 'User'),
    ('admin', 'Admin'),
  )
  role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
  full_name = models.CharField(max_length=150)
  contact = models.CharField(max_length=15)

  def __str__(self):
    return f"{self.username} - {self.full_name} ({self.role})"
  

  
  

