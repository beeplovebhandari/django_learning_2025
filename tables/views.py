
from django.shortcuts import render
from.models import Student

def student(request):
    students = Student.objects.all()
    return render (request , template_name = "tables/student.html", context={"students": students})


def classroom(request):
    return render (request, template_name="tables/classroom.html")
