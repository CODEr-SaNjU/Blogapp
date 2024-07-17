from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'created_date']
        read_only_fields = ['author']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    total_likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'published_date', 'comments', 'total_likes')

    def get_total_likes(self, obj):
        return obj.total_likes


class LikePostSerializer(serializers.Serializer):
    action = serializers.CharField()
    total_likes = serializers.IntegerField()