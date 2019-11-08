from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news-home'),
    path('search/', views.search, name='news-search'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('topic/<int:pk>/', views.list_by_topic, name='list-by-topic'),
    path('topic/', views.list_topics, name='list-topics'),
    path('comment/', views.create_comment_view, name='create-comment'),
]