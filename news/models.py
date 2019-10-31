from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=100)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    datetime = models.DateTimeField(default=timezone.now())
    byline = models.CharField(max_length=150, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200)
    content = models.CharField(max_length=1000)
    article_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    keywords = models.CharField(max_length=255)


class Comment(models.Model):
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now())
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)


class Tag(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

