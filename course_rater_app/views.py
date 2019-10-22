from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from course_rater_app.models import Course, CourseReview, Lab, LabReview, User
from course_rater_app.permissions import IsAdminOrReadOnly
from course_rater_app.serializers import (CourseSerializer,
                                          CourseReviewSerializer,
                                          LabSerializer,
                                          LabReviewSerializer,
                                          UserSerializer)


# Index

@api_view(['GET'])
def api_index(request, format=None):
    """Handle requests to index page."""
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'labs': reverse('lab-list', request=request, format=format),
        'courses': reverse('course-list', request=request, format=format),
    })


# Courses

class CourseList(generics.ListCreateAPIView):
    """Handle requests to 'courses/'."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    """Handle requests to 'courses/<int:pk>/'."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]


# Course Reviews

class CourseReviewList(generics.ListCreateAPIView):
    """Handle requests to 'courses/<int:pk>/reviews/'."""
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user,
                        course=Course.objects.get(id=self.kwargs['pk']))


class CourseReviewDetail(generics.RetrieveUpdateAPIView):
    """Handle requests to 'courses/<int:course_pk>/reviews/<int:review_pk>/'."""
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_url_kwarg = 'review_pk'


# Labs

class LabList(generics.ListCreateAPIView):
    """Handle requests to 'labs/'."""
    queryset = Lab.objects.all()
    serializer_class = LabSerializer
    permission_classes = [IsAdminOrReadOnly]


class LabDetail(generics.RetrieveUpdateDestroyAPIView):
    """Handle requests to 'labs/<int:pk>/'."""
    queryset = Lab.objects.all()
    serializer_class = LabSerializer
    permission_classes = [IsAdminOrReadOnly]


# Lab Reviews

class LabReviewList(generics.ListCreateAPIView):
    """Handle requests to 'labs/<int:pk>/reviews/'."""
    queryset = LabReview.objects.all()
    serializer_class = LabReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user,
                        lab=Lab.objects.get(id=self.kwargs['pk']))


class LabReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """Handle requests to 'labs/<int:lab_pk>/reviews/<int:review_pk>'."""
    queryset = LabReview.objects.all()
    serializer_class = LabReviewSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_url_kwarg = 'review_pk'


# Users

class UserList(generics.ListCreateAPIView):
    """Handle requests to 'users/'."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """Handle requests to 'users/<int:pk>/'."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'username'

