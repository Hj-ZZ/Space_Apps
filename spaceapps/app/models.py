from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model


class User(AbstractUser):
    # Image with no urls
    image = models.ImageField(blank=True, null=True, upload_to="images/%Y/%m/%D/")
    name = models.CharField(max_length=100, blank=True, null=True)
    bio = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return f"Name: {self.username}"

    def followers_count(self):
        return len(self.followers.all())

    def followees_count(self):
        return len(self.followees.all())

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "image": self.image.url,
            "bio": self.bio,
            "followers_count": self.followers_count(),
            "followings_count": self.followees_count(),
        }


class Article(models.Model):
    title = models.CharField(max_length=200)
    url_article = models.URLField(max_length=200)
    post = models.OneToOneField(
        "Post", on_delete=models.SET_NULL, blank=True, null=True
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles",
    )
    image = models.ImageField(blank=True, null=True, upload_to="images/%Y/%m/%D/")

    def __str__(self):
        return self.title

    # TODO: if there is extra time I should add likes.

    def serialize(self):
        return {
            "id": self.id,
            "url_article": self.url_article,
            "content": self.text,
            "image": self.image.url,
        }


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    url_article = models.URLField(max_length=200)

    description = models.TextField(max_length=600)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        "Category", models.SET_NULL, null=True, related_name="posts"
    )
    video = models.FileField(blank=True, null=True, upload_to="videos/%Y/%m/%D/")

    def number_likes(self):
        return self.post_like.all().count()

    def __str__(self):
        return "Post id: {self.id} owner: {self.owner.username}"

    def serialize(self):
        return {
            "id": self.id,
            "owner": self.owner.serialize(),
            "video": self.video.url,
            "description": self.description,
            "url_article": self.url_article,
            "comments": [comment.serialize() for comment in self.comment.all()],
            "date_created": self.date_created.strftime("%b %-d %Y, %-I:%M %p"),
            "like_count": self.number_likes(),
        }


class Like(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="user_likes"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, related_name="post_like"
    )

    # User should not be able to like the same post multiple times
    class Meta:
        unique_together = ["post", "owner"]

    def __str__(self):
        return f"owner: {self.post_id}, post: {self.owner_id} "


class Comment(models.Model):
    text = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="user_comment", null=True
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, default=None, related_name="comment"
    )
    # Replies
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="replies", on_delete=models.CASCADE
    )

    def serialize(self):
        return {
            "id": self.id,
            "owner": self.owner.username,
            "the_comment": self.text,
            "date_created": self.date_created.strftime("%b %-d %Y, %-I:%M %p"),
        }

    def __str__(self):
        return "Comment by {}".format(self.owner.username)


class Follow(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="followees"
    )
    followee = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="followers"
    )

    def serialize(self):
        return {
            "id": self.id,
        }


class Category(models.Model):
    name = models.CharField(max_length=100)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    def __str__(self):
        return self.name
