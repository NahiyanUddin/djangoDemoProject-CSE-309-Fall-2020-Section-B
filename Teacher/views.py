from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
# Create your views here.

def showTeacherPage(request):
    return HttpResponse("<H1>I am a teacher</H1>")

def showTeacherInfoPage(request):
    return render(request,'Teacher/teacherInfoPage.html')

def teacher_register(request):
    if request.method == "POST":
        teacher_form = TeacherForm(request.POST)

        if teacher_form.is_valid() :
            # student_form.save()

            dict = request.POST
            teacher_info = Teacher(user=request.user,
                              name=dict['name'],
                              id=dict['id'],
                              designation=dict['designation'],
                              department = dict['department'])
            teacher_info.save()

            return redirect('home')
        else:
            context = {
                'form' : teacher_form,
            }
            return render(request,'Student/student_register.html',context)

    else:
        teacher_form = TeacherForm()
        context = {
            'form' : teacher_form,
        }
        return render(request,'Student/student_register.html',context )

