from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from Student.models import Student
from django.db.models import Q

@login_required
def homepage(request):

    subject = 'CSE 309 - Fall 2020 - Section B'
    body = render_to_string('user/email_body.html')

    receiver = Student.objects.filter(Q(section='B1') or Q(section='B2'))

    for re in receiver:

        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [re.student_id+'@uap-bd.edu']
        )


    return render(request,'blog/home.html')
