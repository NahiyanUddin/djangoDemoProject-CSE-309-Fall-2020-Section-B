
from django.urls import path
from . import views

urlpatterns = [
    path('',views.showTeacherPage),
    path('info/',views.showTeacherInfoPage),
]
