from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

from users.models import Author


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Article(models.Model):
    headline = models.CharField(max_length=200)
    location = models.CharField(max_length=255, blank=True, null=True)
    publish_date = models.DateField(default=datetime.date.today)
    byline = models.CharField(max_length=150, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200)
    content = models.TextField(max_length=5000)
    article_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    keywords = models.CharField(max_length=255)
    article_url = models.URLField(max_length=500, blank=True, null=True)

    def __repr__(self):
        return self.headline

    def __str__(self):
        return self.headline


class Comment(models.Model):
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now())
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)


class Tag(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class View(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return str(self.user_id) + str(self.article_id)

    def __str__(self):
        return str(self.user_id) + " viewed " + str(self.article_id)


# class Article_URL(models.Model):
#     url = models.URLField(max_length=250)
