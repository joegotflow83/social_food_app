from django.db import models
from django.contrib.auth.models import User


class Friend(models.Model):

    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name


class FriendList(models.Model):

    friends = models.ManyToManyField(Friend)


class Tag(models.Model):

    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Post(models.Model):

    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    body = models.TextField()
    views = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:

        ordering = ['-created']

