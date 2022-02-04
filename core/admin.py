from django.contrib import admin
from core.models import Post, Profile, Relation, Like, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'caption')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('bio', 'user')


@admin.register(Relation)
class RelationCommentAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')
