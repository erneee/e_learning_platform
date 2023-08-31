from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.forms import UserCreationForm



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLES = [
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    ]
    role = models.CharField(max_length=20, choices=ROLES)
    age = models.DateField(null=True, blank=True)
    # Add other fields specific to the UserProfile model if needed


    def __str__(self):
        return f"{self.user}, Age: {self.age}"

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover = models.ImageField('Cover', upload_to='covers', null=True, blank=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instructor_courses', null=True)
    students = models.ManyToManyField(User, through='Enrollment', related_name='enrolled_courses', null=True)


    def __str__(self):
        return self.title

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    #file = models.FileField(upload_to='submissions/')

    def __str__(self):
        return f"Enrollment: {self.student} - {self.course}, Score: {self.score}"


class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='submissions/', null=True)

    def __str__(self):
        return f"{self.submission_date.strftime('%Y-%m-%d')} Assignment: {self.assignment.title} Student: {self.student.f_name} {self.student.l_name}"

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1500)
    due_date = models.DateTimeField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return f"Assignment: {self.title}, Due Date: {self.due_date}"
