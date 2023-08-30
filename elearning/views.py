from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.db.models import Q
from .models import Course, Student, Assignment, Submission, Enrollment

def home(request):
    username = request.user

    context_t = {
        'username': username,

    }
    return render(request, 'home.html', context=context_t)

class CoursesViewList(generic.ListView):
    model = Course
    context_object_name = 'course_list'
    template_name = 'course_list.html'



def search(request):
    query = request.GET.get('search_text')
    search_results = Course.objects.filter(
        Q(title__icontains=query)
    )
    context_t = {
        'query_t': query,
        'search_results_t': search_results,
    }

    return render(request, 'search.html', context_t)