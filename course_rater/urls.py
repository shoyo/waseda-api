"""course_rater URL Configuration"""
from django.urls import path, include


urlpatterns = [
    path('', include('course_rater_app.urls')),
]
