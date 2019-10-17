from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from course_rater_app.models import Course, CourseReview, Lab, LabReview, User
from course_rater_app.permissions import IsOwnerOrReadOnly
from course_rater_app.serializers import (CourseSerializer, CourseReviewSerializer,
                                          LabSerializer, LabReviewSerializer, UserSerializer)


# Index

@api_view(['GET'])
def api_index(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'labs': reverse('lab-list', request=request, format=format),
        'courses': reverse('course-list', request=request, format=format),
    })


# Courses

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# Course Reviews

class CourseReviewList(generics.ListCreateAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)


class CourseReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


# Labs

class LabList(generics.ListCreateAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer


class LabDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer


# Lab Reviews

class LabReviewList(generics.ListCreateAPIView):
    queryset = LabReview.objects.all()
    serializer_class = LabReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)


class LabReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LabReview.objects.all()
    serializer_class = LabReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


# Users

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

