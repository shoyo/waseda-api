import os

from django.urls import path, include
from rest_framework.authtoken import views as authtoken_views
from rest_framework.urlpatterns import format_suffix_patterns

from course_rater_app import views

urlpatterns = [
    # Standard Endpoints
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

    # Endpoint for obtaining an auth token for Token Authentication
    path('api-auth-token/', authtoken_views.obtain_auth_token)
]

# Adding login to browsable API during development
if os.environ['ENVIRONMENT'] == 'development':
    urlpatterns += [
        path('api-auth/', include('rest_framework.urls')),
        path('sentry-debug/', lambda request: 1 / 0)
    ]

