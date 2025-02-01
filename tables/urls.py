from django.urls import path 
from.views import student, classroom, profile

urlpatterns = [
    path ("student/", student, name="student"),
    path ("classroom/", classroom, name="classroom"),
    path('profile/', profile, name = 'profile'),
]