from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='news-home'),
    path('search', views.search, name='news-search'),
]