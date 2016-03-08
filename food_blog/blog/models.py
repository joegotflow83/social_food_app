from django.db import models
from django.contrib.auth.models import User


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

