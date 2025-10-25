import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    author_name = models.CharField(max_length=255)  # Not tied to Django User
    description = models.TextField()
    published_year = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(datetime.date.today().year)])
    blurb = models.CharField(max_length=255, blank=True)
    cover = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["-published_year"]

    def __str__(self):
        return f"{self.title} | written by {self.author_name}"


class Review(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="Reviews")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Reviews")
    body = models.TextField()
    RATING_CHOICES = [(i, i) for i in range(1, 6)]
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)])
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_moderator = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} Profile"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # If the user was just created, make a profile
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # If updating existing user, ensure they have a profile
        UserProfile.objects.get_or_create(user=instance)