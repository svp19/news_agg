from django.urls import path, reverse
from . import views
from .views import TopicCreateView, TagCreateView, UrlCreateView


urlpatterns = [
    path('topic/new/', TopicCreateView.as_view(template_name="news_admin/topic_form.html"), name='topic-create'),
    path('tag/new/', TagCreateView.as_view(template_name="news_admin/tag_form.html"), name='tag-create'),
    path('url/new/', UrlCreateView.as_view(template_name="news_admin/article_url_form.html"), name='url-goto'),
]
