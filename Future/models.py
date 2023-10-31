from django import models 
from django.contrib.auth.models import AbstractUser 
from .manager import *

class Customuser(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    phone=models.CharField( max_length=50)
    is_phone_no_verified=models.BooleanField(default=False)
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = []
    