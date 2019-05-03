from rest_framework.generics import ListAPIView, RetrieveAPIView
from article.models import Article
from article.api.ArticleSerializers import ArticleListSerializer, ArticleDetailSerializer
from django.utils import timezone


class ArticleListView(ListAPIView):
    queryset = Article.objects.all().order_by('-postedDate', "-pk")
    serializer_class = ArticleListSerializer


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
