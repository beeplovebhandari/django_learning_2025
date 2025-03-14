from django.shortcuts import render, redirect
from .models import ClassRoom, Student, StudentProfile


def crud_classroom(request):
    if request.method == "POST":
        name = request.POST.get("name")
        ClassRoom.objects.create(name=name)
        return redirect('crud_classroom')    
    classrooms = ClassRoom.objects.all()
    return render (request, template_name='crud/classroom.html', context={"classrooms": classrooms, "title": "ClassRoom"})



def classroom_delete(request, id):
    classroom = ClassRoom.objects.get(id=id)
    if request.method == "POST":
        classroom.delete()
        return redirect('crud_classroom')
    return render(request, template_name="crud/classroom_delete.html", context={"classroom": classroom})


def classroom_update(request, id):
    classroom = ClassRoom.objects.get(id=id)
    if request.method =="POST":
        name = request.POST.get("name")
        ClassRoom.objects.filter(id=id).update(name=name)
        return redirect("crud_classroom")
    return render(request, template_name="crud/classroom_update.html", context={"classroom": classroom})


def crud_student(request):
    return render(request, template_name="crud/student.html", context={"students": Student.objects.all(), "title": "Student"})



def add_student(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        address = request.POST.get("address")
        contact = request.POST.get("contact")
        pp = request.FILES.get('pp')
        classroom_name = request.POST.get("classroom_name")
        classroom = ClassRoom.objects.get(name=classroom_name)
        student = Student.objects.create(name=name, email=email, age=age, classroom=classroom )
        sp = StudentProfile.objects.create(address=address, contact=contact, student=student)
        if pp: 
            sp.profile_picture = pp
            sp.save()
        return redirect("crud_student")
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="crud/add_student.html", context={"title": "Add Student", "classrooms": classrooms})



def student_delete(request, id):
   student = Student.objects.get(id=id)
   if request.method=="POST":
        student.delete()
        return redirect('crud_student')
   return render(request, template_name="crud/student_delete.html", context={"student":student})



def student_detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, template_name="crud/student_detail.html", context={"title":" Student Detail", "student": student})