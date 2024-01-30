from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model


class ArticleSerialisers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        
    def validate_title(self, value):
        filter_list = ['js', "PHP", "laravel"]
        
        for i in filter_list:
            if i in value:
                raise serializers.ValidationError("این کلمات شامل نمیشوند {}".format(i))
        

class UserSerialisers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"