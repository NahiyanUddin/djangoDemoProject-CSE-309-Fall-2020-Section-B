from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DummyProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures',
                                        default='default.jpg')
    about = models.TextField(blank=True)
    nid = models.CharField(max_length=16,default='')
    gender = models.CharField(max_length=6,default='',blank=True)
    type = models.CharField(max_length=7,default='')

    def __str__(self):
        return 'profile of' + self.user.username



