from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import ReviewForm
from .models import Book

class TestBlogViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Book(
            title="Book title",
            slug="book-title",
            description ="Book description",
            author_name=self.user,
            published_year=2023,
            blurb ="Book blurb",
            cover="placeholder"
        )
        self.post.save()

    def test_render_post_detail_page_with_review_form(self):
        response = self.client.get(reverse(
            'book_detail', args=['book-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Book title", response.content)
        self.assertIn(b"Book description", response.content)
        self.assertIn(b"2023", response.content)
        self.assertIsInstance(
            response.context['review_form'], ReviewForm)
        
    def test_successful_review_submission(self):
        """Test for posting a review on a book"""
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test review.', 'rating': 4
        }
        response = self.client.post(reverse(
            'book_detail', args=['book-title']), post_data, follow=True)
        self.assertEqual(response.status_code, 200)  
        self.assertIn(
            b"Review submitted and awaiting approval",
            response.content
        )