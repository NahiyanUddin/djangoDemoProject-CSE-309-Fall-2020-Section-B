from django.db import models
from Teacher.models import Teacher

# Create your models here.

class Semester(models.Model):
    name = models.CharField(max_length=15)
    session = models.CharField(max_length=20)
    start = models.DateField()
    end = models.DateField()

class Course(models.Model):
    title = models.TextField()
    code = models.CharField(max_length=10)
    instructor = models.ForeignKey(Teacher, null = True,on_delete=models.SET_NULL)
    session = models.CharField(max_length=15)
    semester = models.ForeignKey(Semester,on_delete=models.SET_NULL, null = True)





