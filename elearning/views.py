from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course, UserProfile, Assignment, Submission, Enrollment
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


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


class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'course_detail.html'



def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("User created successfully:", user.username)
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("homepage-url")
        else:
            print("Form errors:", form.errors)
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})