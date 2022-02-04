from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import Relation, Post, Profile, Comment, Like


class RelationSerializer(serializers.ModelSerializer):
    start_user = serializers.StringRelatedField(read_only=True)
    end_user = serializers.StringRelatedField(read_only=True)
    target = serializers.CharField(write_only=True)

    class Meta:
        model = Relation
        fields = ('start_user', 'end_user', 'target')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    post_slug = serializers.SlugField(write_only=True)
    reply_to = serializers.SerializerMethodField(read_only=True)
    reply_to_slug = serializers.SlugField(write_only=True, required=False)

    class Meta:
        model = Comment
        fields = ('user', 'content', 'slug', 'post_slug', 'post', 'reply_to', 'reply_to_slug')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'caption', 'picture']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'first_name', 'last_name', 'bio', 'location', 'profile_picture']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'post']
