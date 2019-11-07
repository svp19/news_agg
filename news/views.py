from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Article, View, Comment, Topic
import news.query as q


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    articles = Article.objects.raw(q.q_all_articles)
    recent = Article.objects.raw(q.q_recent)

    # Fetch Recommended articles by topic
    topics = q.get_topics_by_preference(request.user)
    topic_article_dict = q.get_recommended_by_topic(topics)

    return render(request, 'news/home.html',
                  {'articles': articles, 'recent': recent, 'topic_article_dict': topic_article_dict})


@login_required
def search(request):
    return HttpResponse('Search Results')


class ArticleDetailView(DetailView):
    model = Article

    def get_queryset(self, **kwargs):
        article_id = self.kwargs['pk']
        article = Article.objects.filter(pk=article_id)
        return article

    def get_context_data(self, **kwargs):
        article_id = self.kwargs['pk']

        # insert into views
        article = Article.objects.filter(pk=article_id)[0]
        new_view = View.objects.create(article_id=article, user_id=self.request.user)
        new_view.save()

        # Add tags to context
        context = super().get_context_data(**kwargs)
        article_obj = self.get_object()
        kws = article_obj.keywords
        for punct in ['\'', '[', ']']:
            kws = kws.replace(punct, '')
        kws = kws.split(',')
        context['tags'] = kws

        # Add comments to context
        comments = Comment.objects.filter(article_id=article)
        context['comments'] = comments
        context['num_comments'] = len(comments)
        # print(comments)
        return context


def create_comment_view(request):
    if request.method == "POST":
        article = Article.objects.filter(id=request.POST.get('article_id'))
        Comment.objects.create(
            article_id=article[0],
            comment_by=request.user,
            date_posted=timezone.now(),
            content=request.POST.get('content')
        )
        return redirect('article-detail', pk=article[0].id)
    return redirect('news-home')


def list_by_topic(request, pk=1):
    topic = Topic.objects.filter(id=pk)
    articles = Article.objects.filter(article_topic__in=topic).order_by('-publish_date')
    return render(request, 'news/list_article_by_topic.html', {'articles': articles, 'topic': topic[0].name})


def list_topics(request):
    topics = Topic.objects.all().order_by('name')
    return render(request, 'news/list_topics.html', {'topics': topics})
