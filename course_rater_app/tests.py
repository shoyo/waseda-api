from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token as auth_token_view
from rest_framework.test import (APIClient, APIRequestFactory, APITestCase,
                                 force_authenticate, RequestsClient)

from course_rater_app.fixtures import (courses, labs, users)
from course_rater_app.models import (Course, CourseReview,
                                     Lab, LabReview, User)

import json


class TestEndpointResponses(APITestCase):
    def setUp(self):
        self.client = APIClient()

        for user_args in users:
            User.objects.create(**user_args)
        for course_args in courses:
            Course.objects.create(**course_args)
        for lab_args in labs:
            Lab.objects.create(**lab_args)


    def test_get_responses(self):
        """Assert GET requests to endpoints return 200 OK."""
        for endpoint in ['',
                         '/courses/',
                         '/courses/2/',
                         '/courses/2/reviews/',
                         '/labs/',
                         '/labs/2/',
                         '/labs/2/reviews/',
                         '/users/',
                         '/users/user1/']:
            response = self.client.get(endpoint)
            error = f'Received status {response.status_code} from "{endpoint}"'
            self.assertEqual(response.status_code, 200, error)


    def test_get_reviews_responses(self):
        """Assert GET course and lab review endpoints return 200 OK.

        This test is written separately as it requires additional logic.
        A User object and Course object must exist before a CourseReview object
        can be created.
        """
        # Course and Lab are queried oddly with 'filter()[0]' instead of 'get()'
        # due to buggy automatic primary keys on Docker + Postgres setup
        course = Course.objects.filter(title='Signal Processing')[0]
        lab = Lab.objects.filter(professor='Professor 2')[0]
        user = User.objects.get(username='user1')

        CourseReview.objects.create(
            overall_rating = 3,
            text = 'Lorem ipsum.',
            reviewer = user,
            course = course,
        )
        LabReview.objects.create(
            overall_rating = 3,
            text = 'Lorem ipsum.',
            reviewer = user,
            lab = lab,
        )

        for endpoint in ['/courses/2/reviews/1/',
                         '/labs/2/reviews/1/']:
            response = self.client.get(endpoint)
            error = f'Received status {response.status_code} from "{endpoint}"'
            self.assertEqual(response.status_code, 200, error)


class TestCoursesPOST(APITestCase):
    def setUp(self):
        self.client = APIClient()

        admin_args = users[2]
        assert admin_args['is_staff']

        self.admin = User.objects.create(**admin_args)
        self.token = Token.objects.create(user=self.admin)


    def test_valid_post(self):
        """Assert valid POST requests for courses return correct responses."""

        valid_course_data = {
            "title": "Test Course",
            "course_class_code": "12345",
            "course_code": "ABCDE",
            "level": "Final stage advanced-level undergraduate",
            "category": "Elective Subjects",
            "eligible_year": "2nd year and above",
            "credits": 2,
            "main_language": "English",
            "school": "Fundamental Science and Engineering",
            "campus": "Nishi-Waseda Campus",
            "year": "2020",
            "term": "Fall",
            "academic_disciplines": [
                "discipline A",
                "discipline B",
                "discipline C"
            ],
            "instructors": [
                "professor A",
                "professor B",
                "professor C"
            ],
            "syllabus_urls": [
                "https://example.com/a",
                "https://example.com/b",
                "https://example.com/c"
            ],
            "classrooms": ["classroom A"],
            "sessions": [
                ["Tuesday", "5"],
                ["Thursday", "1"]
            ]
        }
        response = self.client.post('/courses/',
                                    valid_course_data,
                                    format='json',
                                    HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertEqual(response.status_code, 201, response.data)


    def test_missing_fields(self):
        """Assert missing fields are rejected and notified."""
        response = self.client.post('/courses/',
                                    {},
                                    format='json',
                                    HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertEqual(response.status_code, 400)

        # Test for a subset of missing fields for speedup.
        # `response.data` returns a dict mapping missing fields to error messages
        # for 400 Bad Requests
        for field in ["title", "instructors", "sessions"]:
            self.assertTrue(field in response.data)


    def test_invalid_format(self):
        """Assert that schema is validated properly."""
        invalid_course_data = {
            "title": "Test Course",
            "course_class_code": "12345",
            "course_code": "ABCDE",
            "level": "Final stage advanced-level undergraduate",
            "category": "Elective Subjects",
            "eligible_year": "2nd year and above",
            "credits": 2,
            "main_language": "English",
            "school": "Fundamental Science and Engineering",
            "campus": "Nishi-Waseda Campus",
            "year": "2020",
            "term": "Fall",
            "academic_disciplines": [
                "discipline A",
                "discipline B",
                "discipline C"
            ],
            "instructors": [
                "professor A",
                "professor B",
                "professor C"
            ],
            "syllabus_urls": [
                "https://example.com/a",
                "https://example.com/b",
                "not a url" # invalid string format
            ],
            "sessions": [
                ["Tuesday"], # missing subfield
                ["Thursday", "1"]
            ],
            "classrooms": ['51-201']
        }
        response = self.client.post('/courses/',
                                    invalid_course_data,
                                    format='json',
                                    HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertEqual(response.status_code, 400)

        for field in ["syllabus_urls", "sessions"]:
            self.assertTrue(field in response.data, response.data)

