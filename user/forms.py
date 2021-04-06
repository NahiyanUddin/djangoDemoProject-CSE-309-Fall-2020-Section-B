from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User, models
from .models import *
from Student.models import *
from Teacher.models import *


class UserRegistraionForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)

    class Meta:
        model = User
        email = models.EmailField(unique=True)
        fields = [ 'username',
                   'email',
                   'first_name',
                   'last_name',
                   'password1',
                   'password2',
            ]

class UserDetailsForm(forms.Form):
    fname = forms.CharField(label = 'First name',max_length=10)
    lname = forms.CharField(label = 'Last name',max_length=10)


class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=16)
    last_name = forms.CharField(max_length=16)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]


class EditProfileForm(forms.ModelForm):
    about = forms.CharField(required=False)
    profile_picture = forms.ImageField()

    class Meta:
        model = Profile
        fields = [
            'about',
            'profile_picture',
        ]


class RegisterProfileForm(forms.ModelForm):
    gender_choices = [
        ('male','Male'),
        ('male','Female'),
        ('other','Other'),
    ]
    type_choices = [
        ('student','Student'),
        ('teacher','Teacher'),
    ]

    nid = forms.CharField(max_length=16)
    gender = forms.CharField(widget=forms.Select(choices=gender_choices),required=False)
    type = forms.CharField(widget=forms.Select(choices=type_choices))

    class Meta:
        model = Profile
        fields = [
            'nid',
            'gender',
            'type',
        ]




