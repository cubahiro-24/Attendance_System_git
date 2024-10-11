# students/models.py
from django.db import models
from django.utils import timezone

class Student(models.Model):
    first_name = models.CharField(max_length=100, default="Unknown")
    last_name = models.CharField(max_length=100, default="Unknown")
    birthdate = models.DateField(default=timezone.now)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    username = models.CharField(max_length=50, default="Unknown")
    password = models.CharField(max_length=100, default="Unknown")  # In production, consider hashing this

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Lecturer(models.Model):
    first_name = models.CharField(max_length=100, default="Unknown")
    last_name = models.CharField(max_length=100, default="Unknown")
    birthdate = models.DateField(default=timezone.now)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    username = models.CharField(max_length=50, default="Unknown")
    password = models.CharField(max_length=100, default="Unknown")  # In production, consider hashing this

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    course_code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    hours = models.IntegerField()
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)  # Ensure this line exists

    def __str__(self):
        return self.name


class Admin(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)  # You might want to hash this in a real application

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=[
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
    ])
    date = models.DateField()

