from asyncore import read
from typing_extensions import Required
from rest_framework import serializers

from posts.models import Comment, Group, Post, Follow, User
class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group',)
        read_only_fields = ('author',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('__all__')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
        
    following = serializers.SlugRelatedField(queryset=User.objects.all(),
        slug_field='username')



    def validate_user(self, author):
        user = self.context.get('request').user
        if user == author:
            raise serializers.ValidationError(detail='Нельзя подписаться на самого себя')
        return author


    class Meta:
        model = Follow
        fields = ('user', 'following')

