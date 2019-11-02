from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Article, View
from .query import *


@login_required
def home(request):
    articles = Article.objects.raw(q_all)
    recent = Article.objects.all().order_by('-id')
    if len(recent) > 6:
        recent = recent[:6]
    print(recent)
    return render(request, 'news/home.html', {'articles': articles, 'recent': recent})


@login_required
def search(request):
    return HttpResponse('Search Results')


class ArticleDetailView(DetailView):

    model = Article

    def get_queryset(self, **kwargs):
        article_id = self.kwargs['pk']

        # # insert into views
        article = Article.objects.filter(pk=article_id)
        # print("SEE BELOW")
        # print(article[0])
        # new_view = View.objects.create(article_id=article[0], user_id=self.request.user)
        # new_view.save()
        return article

    def get_context_data(self, **kwargs):
        article_id = self.kwargs['pk']

        # insert into views
        article = Article.objects.filter(pk=article_id)
        print("SEE BELOW")
        print(article[0])
        new_view = View.objects.create(article_id=article[0], user_id=self.request.user)
        new_view.save()

        context = super().get_context_data(**kwargs)
        article_obj = self.get_object()
        kws = article_obj.keywords
        for punct in ['\'','[', ']']:
            kws = kws.replace(punct, '')
        kws = kws.split(',')
        context['tags'] = kws
        return context

