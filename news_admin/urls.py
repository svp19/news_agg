from django.urls import path, reverse
from .views import TopicCreateView, TagCreateView, article_url, article_from_url

urlpatterns = [
    path('topic/new/', TopicCreateView.as_view(template_name="news_admin/topic_form.html"), name='topic-create'),
    path('tag/new/', TagCreateView.as_view(template_name="news_admin/tag_form.html"), name='tag-create'),
    path('article-url/new/', article_url, name='article-url'),
    path('article-from-url/new/', article_from_url, name='article-from-url')
]
