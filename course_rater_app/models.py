from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres import fields as postgres_fields
from django.db import models

from .validators import validate_session


RATING_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]


class Course(models.Model):
    """A course model.
    
    Note:
    * "sessions" is a JSONField, so it can't natively perform model-level
      validations of the data format. The input for "sessions" should be
      checked rigorously before creating/updating a Course instance.

      The input of "sessions" should be of the form:
        "sessions": [
            {
                "day": "",
                "period": "",
                "classrooms": ["", ""]
            },
            {
                "day": "",
                "period": "",
                "classrooms": [""]
            },
            ...
        ]


    """
    title = models.CharField(max_length=150)
    course_class_code = models.CharField(max_length=20)
    course_code = models.CharField(max_length=10, blank=True)
    level = models.CharField(max_length=100, blank=True) # Ex. "Final stage advanced-level undergraduate"
    category = models.CharField(max_length=100, blank=True) # Ex. "Elective Subjects"
    eligible_year = models.CharField(max_length=50) # Ex. "4th year and above"
    credits = models.IntegerField()
    main_language = models.CharField(max_length=50)
    school = models.CharField(max_length=100)
    campus = models.CharField(max_length=50, blank=True)
    year = models.CharField(max_length=10)
    term = models.CharField(max_length=50, blank=True)
    academic_disciplines = postgres_fields.ArrayField(
        models.CharField(max_length=100, blank=True),
        size=3,
        blank=True,
        null=True
    )
    instructors = postgres_fields.ArrayField(
        models.CharField(max_length=100, blank=True),
        size=43,
    )
    syllabus_urls = postgres_fields.ArrayField(
        models.URLField(blank=True),
        size=5
    )
    sessions = postgres_fields.JSONField()


class CourseReview(models.Model):
    # Relationships
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 db_column='user_id',
                                 on_delete=models.CASCADE)

    # User reviews
    overall_rating = models.IntegerField(choices=RATING_CHOICES)
    text = models.CharField(max_length=5000)
    anonymous = models.BooleanField(default=False)

    # Metadata
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)


class Lab(models.Model):
    professor = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)


class LabReview(models.Model):
    # Relationships
    lab = models.ForeignKey('Lab', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 db_column='user_id',
                                 on_delete=models.CASCADE)

    # User reviews
    overall_rating = models.IntegerField(choices=RATING_CHOICES)
    text = models.CharField(max_length=5000)
    anonymous = models.BooleanField(default=False)

    # Metadata
    anonymous = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    """A custom User model that extends the built-in AbstractUser model.

    This means that this model also includes the following fields:
    * username (CharField)
    * first_name (CharField)
    * last_name (CharField)
    * is_staff (BooleanField)
    * is_active (BooleanField)
    * date_joined (DateTimeField)
    """
    GRADE_CHOICES = [('B1', "Bachelor's 1"),
                     ('B2', "Bachelor's 2"),
                     ('B3', "Bachelor's 3"),
                     ('B4', "Bachelor's 4"),
                     ('M1', "Master's 1"),
                     ('M2', "Master's 2"),
                     ('D', "PhD"),
                     ('gr', "Graduated"),
                     ('ot', "Other") ]

    email = models.EmailField(unique=True)
    year = models.CharField(max_length=2, choices=GRADE_CHOICES, default='B1')


