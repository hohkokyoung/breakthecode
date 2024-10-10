from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.urls import reverse
from .views import ChallengeHintListView

# Create your tests here.
class ChallengeHintListViewTest(TestCase):

    def setUp(self):
        # Create some sample books to test the list view
        self.factory = APIRequestFactory()  # Initialize the request factory

    def test_get_challenge_hints(self):
        url = reverse("challenge-hints")

        # Initialize the factory and create a GET request
        request = self.factory.get(url, format='json')  # Pass in the URL you'd expect
        
        # Initialize the view with the request
        view = ChallengeHintListView.as_view()

        # Get the response from the view by passing the request
        response = view(request)

        # Verify that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify that the response contains the correct number of books
        self.assertEqual(len(response.data), 3)