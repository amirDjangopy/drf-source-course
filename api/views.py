from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ArticleSerialisers, UserSerialisers
from django.contrib.auth.models import User
from .permissions import IsSuperUser, IsAuthorOrReadOnly, IsStaffOrReadOnly
from blog.models import Article

# Create your views here.


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialisers


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialisers
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)
    
    
class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialisers
    permission_classes = (IsSuperUser ,)
    
    
class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialisers
    permission_classes = (IsSuperUser ,)
    

class RevokeToken(APIView):
    permission_classes = (IsAuthenticated ,)
    
    def delete(self, request):
        request.auth.delete()
        return Response(status=204)
    