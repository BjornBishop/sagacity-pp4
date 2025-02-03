from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import ConsultingAssignment, Comment
from django.contrib.messages import get_messages

class ConsultingAssignmentDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up a user and a consulting assignment for the test
        cls.user = User.objects.create_user(username='testuser', password='testpass')
        cls.assignment = ConsultingAssignment.objects.create(
            title='Market Entry Strategy',
            slug='market-entry-strategy',
            industry='COM',
            status=1,
            author=cls.user,
            required_experience='Market Research / Competitor Analysis / Go to Market / Requirement Analysis',
            role_description='<p>Introduction: Navigating New Markets</p>',
            excerpt='Market Researcher with experience in competitor analysis and Go-To-Market Strategies'
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/assignment/{self.assignment.slug}/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('assignment_detail', args=[self.assignment.slug]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('assignment_detail', args=[self.assignment.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'assignments/detail.html')

    def test_view_context_contains_assignment(self):
        response = self.client.get(reverse('assignment_detail', args=[self.assignment.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertIn('object', response.context)
        self.assertEqual(response.context['object'], self.assignment)

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(username='testuser', password='testpass')
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(reverse('assignment_detail', args=[self.assignment.slug]), post_data)
        
        # Follow the redirect
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('assignment_detail', args=[self.assignment.slug]))
        
        # Check for the success message in the redirected response
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("Comment submitted and awaiting approval" in str(message) for message in messages))
