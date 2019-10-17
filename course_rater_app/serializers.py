from course_rater_app.models import Course, CourseReview, Lab, LabReview, User
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'professor']


class CourseReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.ReadOnlyField(source='reviewer.username')
    course = serializers.HyperlinkedIdentityField(view_name='course-detail', read_only=True)

    class Meta:
        model = CourseReview
        fields = ['id',
                  'course',
                  'reviewer',
                  'overall_rating',
                  'text',
                  'anonymous']


class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = ['id', 'professor', 'topic', 'website']


class LabReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.ReadOnlyField(source='reviewer.username')
    course = serializers.HyperlinkedIdentityField(view_name='lab-detail', read_only=True)

    class Meta:
        model = LabReview
        fields = ['id',
                  'lab',
                  'reviewer',
                  'overall_rating',
                  'text',
                  'anonymous']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'year']
