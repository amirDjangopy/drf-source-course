from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from blog.models import Article
from django.contrib.auth.models import User
from .serializers import ArticleSerialiser, UserSerialiser

# Create your views here.

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser

## User list as detail

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser