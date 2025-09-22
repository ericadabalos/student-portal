from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name
    
    
# Teacher model
class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Subject model
class Subject(models.Model):
    name = models.CharField(max_length=100)
    schedule_day = models.CharField(max_length=20)      # e.g., Monday
    schedule_time = models.CharField(max_length=20)     # e.g., 10:00 AM - 12:00 PM
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Enrollment model
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'subject')  # prevent duplicate enrollments