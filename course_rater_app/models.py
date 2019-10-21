from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


RATING_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]


class Course(models.Model):
    title = models.CharField(max_length=300)
    instructor = models.CharField(max_length=300)
    credits = models.IntegerField()
    level = models.CharField(max_length=200) # Ex. "Final stage advanced-level undergraduate"
    category = models.CharField(max_length=200) # Ex. "Elective Subjects"

    school = models.CharField(max_length=200)
    campus = models.CharField(max_length=200)

    main_language = models.CharField(max_length=100)
    eligible_year = models.CharField(max_length=100) # Ex. "4th year and above"
    course_code = models.CharField(max_length=50)
    course_class_code = models.CharField(max_length=50)

    syllabus_url = models.URLField()

    first_academic_discipline = models.CharField(max_length=200)
    second_academic_discipline = models.CharField(max_length=200)
    third_academic_discipline = models.CharField(max_length=200)

    
    # Can change year-to-year
    classroom = models.CharField(max_length=200)
    year = models.CharField(max_length=10)
    # TODO: parse into following
    term_day_period = models.CharField(max_length=200)
    term = models.CharField(max_length=100, null=True, blank=True)
    day = models.CharField(max_length=100, null=True, blank=True)
    period = models.CharField(max_length=100, null=True, blank=True)



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
    lab = models.ForeignKey('Lab', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 db_column='user_id',
                                 on_delete=models.CASCADE)

    overall_rating = models.IntegerField(choices=RATING_CHOICES)
    text = models.CharField(max_length=5000)

    anonymous = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)


class User(AbstractUser):
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


