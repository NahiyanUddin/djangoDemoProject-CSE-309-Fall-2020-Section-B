from django.contrib.auth.forms import forms
from .models import *

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'name',
            'id',
            'designation',
            'department',
        ]
