from django.shortcuts import render
from django.views.generic import CreateView
from news.models import Topic


class TopicCreateView(CreateView):
    model = Topic
    fields = ['name']
    success_url = '/news/'