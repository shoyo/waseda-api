from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token as auth_view
from rest_framework.test import (APIClient, APIRequestFactory, APITestCase,
                                 force_authenticate, RequestsClient)

from course_rater_app.fixtures import (courses, course_reviews,
                                       labs, lab_reviews, users)
from course_rater_app.models import (Course, CourseReview,
                                     Lab, LabReview, User)


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
                         '/courses/1/',
                         '/courses/1/reviews/',
                         '/labs/',
                         '/labs/1/',
                         '/labs/1/reviews/',
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
        user = User.objects.get(username='user2')
        course = Course.objects.get(pk=2)
        lab = Lab.objects.get(pk=2)

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


class TestAuthentication(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()

        for user_args in users:
            User.objects.create(**user_args)


    def test_get_auth_token(self):
        """Assert that a valid token for Token Authentication is received."""
        pass


    def test_use_auth_token(self):
        """Assert that a token can be used to authenticate."""
        pass

