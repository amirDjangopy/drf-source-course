from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model


class ArticleSerialisers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        

class UserSerialisers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"