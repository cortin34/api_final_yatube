from rest_framework import serializers

from posts.models import Comment, Group, Post
from yatube_api.posts.models import Follow


class PostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(queryset=Group.objects.all(),
                                         slug_field='slug', required=False)
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ('__all__')
        read_only_fields = ('author',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('__all__')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('__all__')


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = ('__all__')