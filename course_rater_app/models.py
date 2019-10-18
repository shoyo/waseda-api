from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


RATING_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]


class Course(models.Model):
    name = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)


class CourseReview(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 db_column='user_id',
                                 on_delete=models.CASCADE)

    overall_rating = models.IntegerField(choices=RATING_CHOICES)
    text = models.CharField(max_length=5000)

    anonymous = models.BooleanField(default=False)
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
    year = models.CharField(max_length=2, choices=GRADE_CHOICES, default='na')


