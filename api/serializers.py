from rest_framework import serializers
from blog.models import Article
from django.contrib.auth.models import User


class ArticleSerialisers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        

class UserSerialisers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"