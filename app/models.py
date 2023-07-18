from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user_name=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    profile_pic=models.ImageField()