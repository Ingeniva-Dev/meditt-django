from rest_framework import viewsets
from api_basic.api import serializers
from api_basic.models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArticleSerializer
    queryset = Article.objects.all()