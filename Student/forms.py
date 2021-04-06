from django.contrib.auth.forms import forms
from .models import *


class StudentForm(forms.ModelForm):
    student_id = forms.CharField(max_length=8)
    student_name = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=19)
    section = forms.CharField(max_length=2)
    class Meta:
        model = StudentInfo
        fields = [
            'student_id',
            'student_name',
            'email',
            'section',
        ]

