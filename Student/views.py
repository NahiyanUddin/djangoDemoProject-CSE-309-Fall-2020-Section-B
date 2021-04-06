from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Student ################
from django.db.models import Q

from . import loaddata

from .forms import *


def showStudentPage(request):
    return HttpResponse("I am a student")

def showStudentInfoPage(request):

    # students = Student.objects.filter(section='B1').order_by('student_name')

    # students = Student.objects.filter(id__range=(83,561))

    # students.delete()

    st = Student.objects.filter(section='B3')
    st.update(section='B1')

    students = Student.objects.filter(Q(student_name__contains='Md') | Q(student_name__contains='Islam'))\
        .order_by('student_name').values_list('student_id','student_name')

    return render(request,"Student/studentInfoPage.html", {'students':students })

def student_register(request):
    if request.method == "POST":
        student_form = StudentForm(request.POST)

        if student_form.is_valid() :
            # student_form.save()

            dict = request.POST
            student_info = StudentInfo(user=request.user,
                              student_id=dict['student_id'],
                              student_name=dict['student_name'],
                              email=dict['email'],
                              section = dict['section'])
            student_info.save()

            return redirect('home')
        else:
            context = {
                'form' : student_form,
            }
            return render(request,'Student/student_register.html',context)

    else:
        student_form = StudentForm()
        context = {
            'form' : student_form,
        }
        return render(request,'Student/student_register.html',context )

