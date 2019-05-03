from django.contrib import admin
from django.urls import path
from article.views import ArticleListView, ArticleDetailView

app_name = 'article'
urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list_view"),
    path("<int:pk>", ArticleDetailView.as_view(), name="article_detail_view"),
]
