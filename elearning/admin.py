from django.contrib import admin
from django.contrib import admin
from .models import Student, Submission, Assignment, Course, Enrollment
# Register your models here.
admin.site.register(Student)
admin.site.register(Submission)
admin.site.register(Assignment)
admin.site.register(Course)
admin.site.register(Enrollment)