from django.db import models
from django.contrib.auth.models import  User
# Create your models here.
class Profile(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE)
     image = models.ImageField(default='profile.jpg', upload_to='profile_pictures')
     location = models.CharField(max_length=100)
