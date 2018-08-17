from django.db import models
from django.utils import timezone
from profile_api.models import UserProfile


class Post(models.Model):
    """
    represents the data structure of
    posts model
    """
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, max_length=255)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
