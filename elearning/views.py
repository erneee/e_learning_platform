from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.db.models import Q
from .models import Course, Student, Assignment, Submission, Enrollment

def home(request):
    return render(request, 'home.html')

