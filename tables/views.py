
from django.shortcuts import render
from.models import Student, StudentProfile

def student(request):
    students = Student.objects.all()
    return render (request , template_name = "tables/student.html", context={"students": students})


def classroom(request):
    return render (request, template_name="tables/classroom.html")

def profile (request):
    return render (request, template_name="tables/profile.html", context= {"profiles":StudentProfile.objects.all} )