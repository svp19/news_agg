from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Article, View, Comment, Topic
from .query import *


@login_required
def home(request):
    articles = Article.objects.raw(q_all)
    recent = Article.objects.raw(q_recent)

    # Fetch Recommended articles by topic
    topics = Topic.objects.all()
    topic_article_dict = {}
    for topic in topics:
        topic_article_dict[topic.name] = Article.objects.filter(article_topic=topic)

    print('Special Query')

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


# def create_comment_view(request):
#     print("Enter COMMENT VIEW")
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         print("POST")
#         # if form.is_valid():
#         # print("DATA", comment)
#         # article_pk = request.POST.get('article_pk')
#         # comment.comment_by = request.user
#         # comment.article = Article.objects.filter(pk=article_pk)
#         # comment.date_posted = timezone.now()
#         # print("COMMENT!!!:", comment.content)
#         # comment.save()
#         return render(request, 'news_admin/tag_form.html', {'form': form})
#
#     else:
#         form = CommentForm()
#         print("NOT POST")
#     return render(request, 'news_admin/tag_form.html', {'form': form})


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
