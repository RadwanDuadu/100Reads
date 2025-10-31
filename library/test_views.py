from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import ReviewForm
from .models import Book, UserProfile, Review


class TestBookViews(TestCase):
    """Tests for book detail view and review submission"""

    def setUp(self):
        """Create a test user and sample book"""
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Book.objects.create(
            title="Book title",
            slug="book-title",
            description="Book description",
            author_name=self.user,
            published_year=2023,
            blurb="Book blurb",
            cover="placeholder"
        )

    def test_render_post_detail_page_with_review_form(self):
        """Ensure book detail page renders correctly with review form"""
        response = self.client.get(reverse('book_detail', args=['book-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Book title", response.content)
        self.assertIn(b"Book description", response.content)
        self.assertIn(b"2023", response.content)
        self.assertIsInstance(response.context['review_form'], ReviewForm)

    def test_successful_review_submission(self):
        """Test successful review submission by logged-in user"""
        self.client.login(username="myUsername", password="myPassword")
        post_data = {'body': 'This is a test review.', 'rating': 4}
        response = self.client.post(
            reverse('book_detail', args=['book-title']),
            post_data,
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Review submitted and awaiting approval", response.content
        )


class ModeratorActionsTest(TestCase):
    """Tests for moderator and user actions on reviews"""

    def setUp(self):
        """Create users, book, and review for testing"""
        self.user = User.objects.create_user(
            username="user",
            password="pass123"
            )
        self.moderator = User.objects.create_user(
            username="mod", password="pass123"
        )

        # Mark moderator as having moderator privileges
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
        """Moderators can approve pending reviews"""
        self.client.login(username="mod", password="pass123")
        response = self.client.post(
            reverse("approve_review", args=[self.review.id])
        )
        self.review.refresh_from_db()
        self.assertTrue(self.review.approved)
        self.assertEqual(response.status_code, 302)

    def test_non_moderator_cannot_approve_review(self):
        """Non-moderators cannot approve reviews"""
        self.client.login(username="user", password="pass123")
        response = self.client.post(
            reverse("approve_review", args=[self.review.id])
        )
        self.review.refresh_from_db()
        self.assertFalse(self.review.approved)
        self.assertIn(response.status_code, [302, 403])

    def test_moderator_can_delete_any_review(self):
        """Moderators can delete reviews from any user"""
        self.client.login(username="mod", password="pass123")
        response = self.client.post(
            reverse("delete_review", args=[self.review.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Review.objects.filter(id=self.review.id).exists())

    def test_user_can_delete_own_review(self):
        """Users can delete only their own reviews"""
        self.client.login(username="user", password="pass123")
        own_review = Review.objects.create(
            book=self.book,
            author=self.user,
            body="Own review",
            rating=4
        )
        response = self.client.post(
            reverse("delete_review", args=[own_review.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Review.objects.filter(id=own_review.id).exists())

    def test_user_cannot_delete_others_review(self):
        """Regular users cannot delete reviews by other users"""
        other_user = User.objects.create_user(
            username="other", password="pass123"
        )
        self.client.login(username="other", password="pass123")
        response = self.client.post(
            reverse("delete_review", args=[self.review.id])
        )
        self.assertIn(response.status_code, [302, 403])
        self.assertTrue(Review.objects.filter(id=self.review.id).exists())

    def test_unauthenticated_user_cannot_delete(self):
        """Unauthenticated users cannot delete reviews"""
        response = self.client.post(
            reverse("delete_review", args=[self.review.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Review.objects.filter(id=self.review.id).exists())
