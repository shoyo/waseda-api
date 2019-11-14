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
                         '/labs/2/reviews/']:
            response = self.client.get(endpoint)
            error = f'Received status {response.status_code} from "{endpoint}"'
            self.assertEqual(response.status_code, 200, error)


    def test_get_reviews_responses(self):
        """Assert GET course and lab review endpoints return 200 OK.

        This test is written separately as it requires additional logic.
        A User object and Course object must exist before a CourseReview object
        can be created.
        """
        course = Course.objects.get(pk=2)
        lab = Lab.objects.get(pk=2)
        user = User.objects.get(pk=1)

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


    def test_get_users_response(self):
        """Assert that non-admin cannot GET the /users/ endpoint."""
        username = User.objects.get(pk=2).username
        for endpoint in ['/users/',
                         f'/users/{username}/']:
            response = self.client.get(endpoint)
            self.assertEqual(response.status_code, 403)


    def test_get_admin_users_response(self):
        """Assert that admin can GET the /users/ endpoint."""
        admin = User.objects.get(pk=3)
        assert admin.is_staff
        token = Token.objects.create(user=admin)

        username = User.objects.get(pk=2).username
        for endpoint in ['/users/',
                         f'/users/{username}/']:
            response = self.client.get(endpoint,
                                       HTTP_AUTHORIZATION=f'Token {token}')
            self.assertEqual(response.status_code, 200, response.data)


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
            "campus": "Nishi-Waseda Campus",
            "year": "2020",
            "term": "Fall",
            "syllabus_url": "https://example.com/a",
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
            "schools": [
                "School of Fundamental Science and Engineering",
                "School of Advanced Science and Engineering",
                "School fo Creative Science and Engineering"
            ],
            "sessions": [
                {
                    "day": "Tuesday",
                    "period": "2",
                    "classrooms": ["53-102"]
                },
                {
                    "day": "Friday",
                    "period": "2",
                    "classrooms": ["55-102", "22-123"]
                }
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
        """Assert that schema is validated properly.

        Note: Currently the `sessions` field is a JSON field that is not
        rigorously validated.
        """
        invalid_course_data = {
            "title": "Test Course",
            "course_class_code": "12345",
            "course_code": "ABCDE",
            "level": "Final stage advanced-level undergraduate",
            "category": "Elective Subjects",
            "eligible_year": "2nd year and above",
            "credits": 2,
            "main_language": "English",
            "campus": "Nishi-Waseda Campus",
            "year": "2020",
            "term": "Fall",
            "syllabus_url": "not a url", # invalid string format
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
            "schools": [
                "School of Fundamental Science and Engineering",
                "School of Advanced Science and Engineering",
                "School fo Creative Science and Engineering"
            ],
            "sessions": [
                {
                    "day": "Tuesday",
                    "period": "2",
                    # missing subfield (not currently caught)
                },
                {
                    "day": "Friday",
                    "period": "2",
                    "classrooms": ["55-102", "22-123"]
                }
            ]
        }
        response = self.client.post('/courses/',
                                    invalid_course_data,
                                    format='json',
                                    HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertEqual(response.status_code, 400)

        # TODO: validate that sessions JSON field is formatted correctly
        for field in ["syllabus_url"]:
            self.assertTrue(field in response.data, response.data)


    def test_allow_some_missing_fields(self):
        """Assert that the fields listed below are allowed to be blank:

        - academic_disciplines
        - campus
        - category
        - course_code
        - level
        - term
        """
        valid_course_data = {
            "title": "Test Course",
            "course_class_code": "12345",
            "eligible_year": "2nd year and above",
            "credits": 2,
            "main_language": "English",
            "syllabus_urls": "https://example.com/a",
            "schools": [
                "Fundamental Science and Engineering",
            ],
            "year": "2020",
            "instructors": [
                "professor A",
                "professor B",
                "professor C"
            ],
            "sessions": [
                {
                    "day": "Tuesday",
                    "period": "2",
                    "classrooms": ["53-102"]
                },
                {
                    "day": "Friday",
                    "period": "2",
                    "classrooms": ["55-102", "22-123"]
                }
            ]
        }
        response = self.client.post('/courses/',
                                    valid_course_data,
                                    format='json',
                                    HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertEqual(response.status_code, 201, response.data)
