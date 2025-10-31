from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):

    def test_form_is_valid(self):
        review_form = ReviewForm({'body': 'This is a great book!', 'rating': 5})
        self.assertTrue(review_form.is_valid(), msg='Review Form is not valid')
 
    def test_body_is_invalid(self):
        review_form = ReviewForm({'body': '', 'rating': 3})
        self.assertFalse(review_form.is_valid(), msg="Review is missing body, Form is valid")

    def test_rating_is_invalid(self):
        review_form = ReviewForm({'body': 'This is a bad book', 'rating': ''})
        self.assertFalse(review_form.is_valid(), msg="Review is missing body, Form is valid")
