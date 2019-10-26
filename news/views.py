from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# Create your views here.
def home(request):
    articles = Article.objects.all()
    return render(request, 'news/home.html', {'articles': articles})


def search(request):
    return HttpResponse('Search Results')
