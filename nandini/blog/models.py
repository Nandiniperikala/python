from django.db import models
from django.views import View

class Teacher(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=255, default='Unknown')

def __str__(self):
        return self.name
# Create your models here.

def create_teacher(number_value):
    new_teacher = Teacher(number=number_value)
    new_teacher.save()

# Retrieving all teachers from the database
def get_all_teachers():
    teachers = Teacher.objects.all()
    return teachers

# Retrieving a specific teacher by ID from the database
def get_teacher_by_id(teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    return teacher

# Updating a teacher's information
def update_teacher(teacher_id, new_number_value):
    teacher = Teacher.objects.get(pk=teacher_id)
    teacher.number = new_number_value
    teacher.save()

# Deleting a teacher from the database
def delete_teacher(teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    teacher.delete()


