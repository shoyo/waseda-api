from course_rater_app.models import Course, CourseReview, Lab, LabReview, User
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'professor']


class CourseReviewSerializer(serializers.ModelSerializer):
    course_url = serializers.HyperlinkedRelatedField(
        view_name='course-detail',
        lookup_url_kwarg='pk',
        read_only=True,
        source='course',
    )
    reviewer_url = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        lookup_url_kwarg='pk',
        read_only=True,
        source='reviewer',
    )

    class Meta:
        model = CourseReview
        fields = ['id',
                  'overall_rating',
                  'text',
                  'anonymous',
                  'course_url',
                  'reviewer_url',]


class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = ['id', 'professor', 'topic', 'website']


class LabReviewSerializer(serializers.ModelSerializer):
    lab_url = serializers.HyperlinkedRelatedField(
        view_name='lab-detail',
        lookup_url_kwarg='pk',
        read_only=True,
        source='lab',
    )
    reviewer_url = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        lookup_url_kwarg='pk',
        read_only=True,
        source='reviewer',
    )

    class Meta:
        model = LabReview
        fields = ['id',
                  'overall_rating',
                  'text',
                  'anonymous',
                  'lab_url',
                  'reviewer_url',]


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    lab_reviews = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='lab-review-detail',
    )

    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'year',
                  'password',
                  'lab_reviews',]

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

