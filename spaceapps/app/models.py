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
    text = models.TextField()
    Authors = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="articles"
    )
    post = models.OneToOneField("Post", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
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
            "title": self.title,
            "content": self.text,
            "image": self.image.url,
            "date": self.date_created,
            "authors": self.Authors_id,
        }
