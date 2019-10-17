from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from course_rater_app import views

urlpatterns = [
    path('courses/', views.CourseList.as_view()),
    path('courses/<int:pk>/', views.CourseDetail.as_view()),
    path('labs/', views.LabList.as_view()),
    path('labs/<int:pk>/', views.LabDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
