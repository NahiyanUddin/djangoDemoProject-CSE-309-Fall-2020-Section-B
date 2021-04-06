from django.urls import path
from . import views


urlpatterns = [
    path('',views.showStudentPage),
    path('info/',views.showStudentInfoPage),
]
