from django.contrib import admin
from .models import UserProfile, Submission, Assignment, Course, Enrollment
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Submission)
admin.site.register(Assignment)
admin.site.register(Course)
admin.site.register(Enrollment)