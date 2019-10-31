from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .query import *


@login_required
def home(request):
    articles = Article.objects.raw(q_all)
    print(articles)
    return render(request, 'news/home.html', {'articles': articles})


@login_required
def search(request):
    return HttpResponse('Search Results')
