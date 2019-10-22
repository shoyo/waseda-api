from course_rater_app.models import Course, CourseReview, Lab, LabReview, User
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
    

class CourseReviewSerializer(serializers.ModelSerializer):
    course_url = serializers.HyperlinkedRelatedField(
        view_name='course-detail',
        lookup_url_kwarg='pk',
        read_only=True,
        source='course',
    )
    reviewer_url = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        lookup_field='username',
        lookup_url_kwarg='username',
        read_only=True,
        source='reviewer',
    )
    datetime_created = serializers.ReadOnlyField()
    datetime_updated = serializers.ReadOnlyField()

    class Meta:
        model = CourseReview
        fields = ['id',
                  'overall_rating',
                  'text',
                  'anonymous',
                  'course_url',
                  'reviewer_url',
                  'datetime_created',
                  'datetime_updated',]


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
        lookup_field='username',
        lookup_url_kwarg='username',
        read_only=True,
        source='reviewer',
    )
    datetime_created = serializers.ReadOnlyField()
    datetime_updated = serializers.ReadOnlyField()

    class Meta:
        model = LabReview
        fields = ['id',
                  'overall_rating',
                  'text',
                  'anonymous',
                  'lab_url',
                  'reviewer_url',
                  'datetime_created',
                  'datetime_updated',]


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'email',
                  'year',
                  'date_joined',
                  'password',]

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

