from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teacher(models.Model):
    name = models.TextField()
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=20)
    department = models.CharField(max_length=3)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
