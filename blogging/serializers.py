from django.contrib.auth.models import User
from blogging.models import Post, Category
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email"]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["url", "name", "description", "posts"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            "url",
            "title",
            "text",
            "created_date",
            "modified_date",
            "published_date",
            "author",
        ]
