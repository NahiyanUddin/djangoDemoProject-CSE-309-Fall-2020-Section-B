from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    student_id = models.CharField(max_length=8, db_column='Student ID')
    student_name = models.CharField(max_length=25, db_column='Student Name')
    email = models.EmailField(max_length=19 , db_column='Email')
    section = models.CharField(max_length=2, db_column='Section')

    class Meta:
        db_table = 'Student-info'

    def __str__(self):
        return str(self.student_id + '-' + self.student_name)


class StudentInfo(models.Model):
    student_id = models.CharField(max_length=8, db_column='Student ID')
    student_name = models.CharField(max_length=25, db_column='Student Name')
    email = models.EmailField(max_length=19 , db_column='Email')
    section = models.CharField(max_length=2, db_column='Section')
    user = models.OneToOneField(User,on_delete=models.CASCADE,default='')


