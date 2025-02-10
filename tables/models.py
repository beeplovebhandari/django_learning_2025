
from django.db import models

class ClassRoom(models.Model):
    name = models.CharField(max_length=20)


class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.CharField(max_length=20)
    bio = models.TextField()
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="classroom_students", null=True, blank=True)

    
    def __str__(self):
        return self.name
 
    
class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    contact = models.IntegerField()
    roll_no = models.IntegerField()


    










 