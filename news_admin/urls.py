from django.urls import path, reverse
from .views import TopicCreateView, TagCreateView, article_url, article_from_url

urlpatterns = [
    path('topic/new/', TopicCreateView.as_view(template_name="news_admin/topic_form.html"), name='create-topic'),
    path('tag/new/', TagCreateView.as_view(template_name="news_admin/tag_form.html"), name='create-tag'),
    path('article-url/new/', article_url, name='create-article-url'),
    path('article-from-url/new/', article_from_url, name='article-from-url')
    # if changed, also change in article_url.html
]
