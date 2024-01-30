from rest_framework.viewsets import ModelViewSet
from .serializers import ArticleSerialisers, UserSerialisers
from django.contrib.auth import get_user_model
from .permissions import IsSuperUser, IsAuthorOrReadOnly, IsStaffOrReadOnly
from blog.models import Article

# Create your views here.


# class ArticleList(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerialisers


# class ArticleDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerialisers
#     permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialisers
    filterset_fields = ['status', 'author__username',]
    ordering_fields = ['publish', 'status']
    search_fields = [
        'title', 'content',
        'author__username', 
        'author__first_name', 
        'author__last_name'
        ]
    
    
    def get_permissions(self):  
        if self.action == ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


# class UserList(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerialisers
#     permission_classes = (IsSuperUser ,)
    
    
# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerialisers
#     permission_classes = (IsSuperUser ,)


class UserViewSet(ModelViewSet):
     queryset = get_user_model().objects.all()
     serializer_class = UserSerialisers
     permission_classes = (IsSuperUser,)

