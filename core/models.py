from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    bio = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    profile_picture = models.ImageField(upload_to="images", null=True, blank=True)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    picture = models.ImageField(upload_to="images", null=True, blank=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return str(self.user)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    caption = models.TextField()

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return "{} on {}".format(str(self.user), str(self.post))


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'like'
        verbose_name_plural = 'likes'

    def __str__(self):
        return "{} on {}".format(str(self.user), str(self.post))


class Relation(models.Model):
    from_user = models.ForeignKey(User, related_name='followings', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'relation'
        verbose_name_plural = 'relations'

    def __str__(self):
        return "({follower}) >>> ({following})".format(
            follower=self.from_user.username,
            following=self.to_user.username,
        )
