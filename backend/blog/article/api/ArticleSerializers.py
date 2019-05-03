from rest_framework import serializers
from article.models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('pk', 'title', 'text', 'postedDate')


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('pk', 'title', 'text', 'postedDate')
