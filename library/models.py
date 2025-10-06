from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Published"),
)

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    author_name = models.CharField(max_length=255)  # Not tied to Django User
    description = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    blurb = models.TextField(blank=True)

    class Meta:
        ordering = ["-published_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author_name}"
    
class Review(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="Reviews")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Reviews")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"