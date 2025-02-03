from django.test import TestCase
from django.urls import reverse
from .models import About, CollaborationRequest
from .forms import CollaborateForm
from django.contrib.messages import get_messages

class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About(
            title="About Me", content="This is about me.")
        self.about_content.save()

    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(
            response.context['form'], CollaborateForm)

    def test_successful_collaboration_request_submission(self):
        """Test for a user requesting a collaboration"""
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        response = self.client.post(reverse('about'), post_data)
        
        # Follow the redirect
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('about'))
        
        # Check for the success message in the redirected response
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("Your application request has been submitted successfully. We should respond within the week" in str(message) for message in messages))
