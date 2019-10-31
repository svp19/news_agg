from django.shortcuts import render
from django.views.generic import CreateView
from news.models import Topic, Tag, Article_URL


class TopicCreateView(CreateView):
    model = Topic
    fields = ['name']
    success_url = '/news/'


class TagCreateView(CreateView):
    model = Tag
    fields = ['article_id', 'name']
    success_url = '/news/'


class UrlCreateView(CreateView):
    model = Article_URL
    fields = ['url']
    success_url = '/news/'
