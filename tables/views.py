
from django.shortcuts import render
from.models import Student, StudentProfile, ClassRoom

def student(request):
    students = Student.objects.all()
    return render (request , template_name = "tables/student.html", context={"students": students})


def classroom(request):
    classroom = ClassRoom.objects.all()
    student = Student.objects.all()
    return render (request, template_name="tables/classroom.html",context={"classrooms" :classroom, "students": student})

def profile (request):
    return render (request, template_name="tables/profile.html", context= {"profiles":StudentProfile.objects.all} )