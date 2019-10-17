from django.urls import path
from course_rater_app import views

urlpatterns = [
    path('courses/', views.all_courses),
    path('courses/<int:pk>/', views.),
]
