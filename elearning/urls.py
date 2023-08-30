from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage-url'),
    path('courses/', views.CoursesViewList.as_view(), name='courses-list-url'),
    path('search/', views.search, name='search'),
]