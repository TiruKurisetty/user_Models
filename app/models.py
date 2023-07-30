from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    profile_pic=models.ImageField()