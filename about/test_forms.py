from django.test import TestCase
from about.forms import CollaborateForm

class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """Test for all fields being valid"""
        form_data = {
            'name': 'Test User',
            'email': 'test@test.com',
            'message': 'This is a test message.'
        }
        form = CollaborateForm(data=form_data)
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid"
        )

    def test_email_is_required(self):
        """Test for the 'email' field"""
        form = CollaborateForm({
            'name': 'Matt',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )

    def test_message_is_required(self):
        """Test for the 'message' field"""
        form = CollaborateForm({
            'name': 'Matt',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid"
        )

    def test_invalid_email_format(self):
        """Test for invalid email format"""
        form = CollaborateForm({
            'name': 'Matt',
            'email': 'invalid-email',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Invalid email format provided, but the form is valid"
        )

    def test_name_and_message_are_required(self):
        """Test for both 'name' and 'message' fields required"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Name and message were not provided, but the form is valid"
        )

    def test_email_and_message_are_required(self):
        """Test for both 'email' and 'message' fields required"""
        form = CollaborateForm({
            'name': 'Matt',
            'email': '',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Email and message were not provided, but the form is valid"
        )
