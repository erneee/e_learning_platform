from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='homepage-url'),
    path('courses/', views.CoursesViewList.as_view(), name='courses-list-url'),
    path('courses/<int:pk>', views.CourseDetailView.as_view(), name='course-one'),
    path('search/', views.search, name='search'),
    path("register/", views.register_request, name="register"),
]