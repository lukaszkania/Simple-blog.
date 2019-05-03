from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article
from django.utils import timezone
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = "article/ArticleListView.html"
    ordering = ['-postedDate']
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article/ArticleDetailView.html"
