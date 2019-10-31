from django.urls import path, reverse
from . import views
from .views import TopicCreateView


urlpatterns = [
    path('topic/new/', TopicCreateView.as_view(template_name="news_admin/topic_form.html"), name='topic-create'),
]
