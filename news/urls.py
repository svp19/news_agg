from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news-home'),
    path('search', views.search, name='news-search'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
]