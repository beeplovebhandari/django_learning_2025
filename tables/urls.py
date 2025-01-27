from django.urls import path 
from.views import student, classroom

urlpatterns = [
    path ("student/", student, name="student"),
    path ("classroom/", classroom, name="classroom"),
]