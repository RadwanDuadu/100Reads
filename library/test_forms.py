from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):

    def test_form_is_valid(self):
        review_form = ReviewForm({'body': 'This is a great book!', 'rating': 5})
        self.assertTrue(review_form.is_valid(), msg='Review Form is not valid')
    
    def test_form_is_invalid(self):
        review_form = ReviewForm({'body': ''})
        self.assertFalse(review_form.is_valid(), msg="Review Form is valid")