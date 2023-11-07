from rest_framework import serializers
from blog.models import Article

class ArticleSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        # fields = ("title", "slug", "author""content", "publish", "status" )
        # exclude = ("created", "updated") ## همه فیلد ها به جز مقدار خاسته شده