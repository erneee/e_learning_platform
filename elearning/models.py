from django.db import models


class Student(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=3)
    # email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name}, Age: {self.age}"

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1500)
    students = models.ManyToManyField('Student', through='Enrollment')

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    #file = models.FileField(upload_to='submissions/')

    def __str__(self):
        return f"Enrollment: {self.student} - {self.course}, Score: {self.score}"


class Submission(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.submission_date.strftime('%Y-%m-%d')} Assignment: {self.assignment.title} Student: {self.student.f_name} {self.student.l_name}"

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1500)
    due_date = models.DateTimeField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return f"Assignment: {self.title}, Due Date: {self.due_date}"
