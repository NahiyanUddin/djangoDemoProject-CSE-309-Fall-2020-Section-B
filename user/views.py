from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import DummyProfile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

@login_required
def profile(request):
    pro_pic = request.user.profile.profile_picture.url

    return render(request,'user/profile.html', {'pro_pic' : pro_pic})

@login_required
def edit_profile(request):
    pro_pic = request.user.profile.profile_picture.url

    edit_user_form = EditUserForm(instance=request.user)
    edit_profile_form = EditProfileForm(instance=request.user.profile)

    context = {
        "edit_user_form" : edit_user_form,
        "edit_profile_form" : edit_profile_form,
        'pro_pic' : pro_pic,
    }

    if request.method == "POST":
        edit_user_form = EditUserForm(request.POST,
                                      instance=request.user)
        edit_profile_form = EditProfileForm(request.POST,
                                            request.FILES,
                                            instance=request.user.profile)
        if edit_user_form.is_valid() and edit_user_form.is_valid():
            edit_user_form.save()
            edit_profile_form.save()

            return redirect('user-profile')
        else:
            return render(request,'user/edit_profile.html', context)

    return render(request,'user/edit_profile.html', context)

def register(request):
    if request.method == "POST":
        registration_form = UserRegistraionForm(request.POST)
        register_profile_form = RegisterProfileForm(request.POST)

        if registration_form.is_valid() and register_profile_form.is_valid():
            registration_form.save()

            # auto login
            username = registration_form.cleaned_data.get('username')
            password = registration_form.cleaned_data.get('password1')
            # print(username)

            new_user = authenticate(username=username, password=password)
            login(request,new_user)

             # profile row create
            dict = request.POST
            profile = Profile(user=new_user,
                              nid=dict['nid'],
                              type=dict['type'],
                              gender=dict['gender'])
            profile.save()

            ##### welcome mail send

            subject = 'Welcome to our class'
            body = render_to_string('user/intro_email.html')

            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [new_user.email]
            )

            if dict['type'] == 'student':
                return redirect('student_register')
            else:
                return redirect('teacher_register')


            return redirect('home')
        else:
            context = {
                'form' : registration_form,
                'r_form':register_profile_form
            }
            return render(request,'user/register.html',context)

    else:
        registration_form = UserRegistraionForm()
        register_profile_form = RegisterProfileForm()
        context = {
            'form' : registration_form,
            'r_form':register_profile_form
        }
        return render(request,'user/register.html',context )
