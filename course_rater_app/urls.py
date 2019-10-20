import os

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from course_rater_app import views

urlpatterns = [
    path('', views.api_index),
    path('courses/',
         views.CourseList.as_view(),
         name='course-list'),
    path('courses/<int:pk>/',
         views.CourseDetail.as_view(),
         name='course-detail'),
    path('courses/<int:pk>/reviews/',
         views.CourseReviewList.as_view(),
         name='course-review-list'),
    path('courses/<int:course_pk>/reviews/<int:review_pk>/',
         views.CourseReviewDetail.as_view(),
         name='course-review-detail'),
    path('labs/',
         views.LabList.as_view(),
         name='lab-list'),
    path('labs/<int:pk>/',
         views.LabDetail.as_view(),
         name='lab-detail'),
    path('labs/<int:pk>/reviews/',
         views.LabReviewList.as_view(),
         name='lab-review-list'),
    path('labs/<int:course_pk>/reviews/<int:review_pk>/',
         views.LabReviewDetail.as_view(),
         name='lab-review-detail'),
    path('users/',
         views.UserList.as_view(),
         name='user-list'),
    path('users/<slug:username>/',
         views.UserDetail.as_view(),
         name='user-detail'),
]

if os.environ['ENVIRONMENT'] == 'development':
    urlpatterns += [
        path('api-auth/', include('rest_framework.urls')),
    ]
