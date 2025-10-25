from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import ReviewForm
from .models import Book, UserProfile, Review

class TestBookViews(TestCase):

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


class ModeratorActionsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="pass123")
        self.moderator = User.objects.create_user(username="mod", password="pass123")

        # ✅ Update existing profile instead of creating new
        self.moderator.userprofile.is_moderator = True
        self.moderator.userprofile.save()

        self.book = Book.objects.create(
            title="Sample Book",
            slug="sample-book",
            description="Desc",
            author_name=self.user,
            published_year=2024,
            blurb="blurb",
            cover="placeholder"
        )

        self.review = Review.objects.create(
            book=self.book,
            author=self.user,
            body="Test review",
            rating=3,
            approved=False
        )

    def test_moderator_can_approve_review(self):
        self.client.login(username="mod", password="pass123")
        response = self.client.post(reverse("approve_review", args=[self.review.id]))
        self.review.refresh_from_db()
        self.assertTrue(self.review.approved)
        self.assertEqual(response.status_code, 302)  # redirect after approval

    def test_non_moderator_cannot_approve_review(self):
        self.client.login(username="user", password="pass123")
        response = self.client.post(reverse("approve_review", args=[self.review.id]))
        self.review.refresh_from_db()
        self.assertFalse(self.review.approved)
        self.assertIn(response.status_code, [302, 403])  # redirect or forbidden

    def test_moderator_can_delete_any_review(self):
        """Moderators can delete reviews regardless of author"""
        self.client.login(username="mod", password="pass123")
        response = self.client.post(reverse("delete_review", args=[self.review.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Review.objects.filter(id=self.review.id).exists())

    def test_user_can_delete_own_review(self):
        """Users can delete their own reviews"""
        self.client.login(username="user", password="pass123")
        own_review = Review.objects.create(
            book=self.book, author=self.user, body="Own review", rating=4
        )
        response = self.client.post(reverse("delete_review", args=[own_review.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Review.objects.filter(id=own_review.id).exists())

    def test_user_cannot_delete_others_review(self):
        """Regular users cannot delete others' reviews"""
        other_user = User.objects.create_user(username="other", password="pass123")
        self.client.login(username="other", password="pass123")
        response = self.client.post(reverse("delete_review", args=[self.review.id]))
        self.assertIn(response.status_code, [302, 403])  # redirect or forbidden
        self.assertTrue(Review.objects.filter(id=self.review.id).exists())

    def test_unauthenticated_user_cannot_delete(self):
        """Unauthenticated users cannot delete reviews"""
        response = self.client.post(reverse("delete_review", args=[self.review.id]))
        self.assertEqual(response.status_code, 302)  # likely redirected to login
        self.assertTrue(Review.objects.filter(id=self.review.id).exists())