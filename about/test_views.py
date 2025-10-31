from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import ContactForm


# Test class for About view
class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About(
            title="About Me", content="This is about me.")
        self.about_content.save()

    def test_render_about_page_with_contact_form(self):
        """Verifies get request for about me containing a contact form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(
            response.context['contact_form'], ContactForm)

    def test_successful_contact_request_submission(self):
        """Test for a user requesting a contact"""
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Contact request received! I endeavour to respond ' 
            'within 2 working days.', response.content)
