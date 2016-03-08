from django.db import models
from django.contrib.auth.models import User


food_types = (
    ('Fruit', 'Fruit'),
    ('Vegetable', 'Vegetable')
)


class Friend(models.Model):

    username = models.CharField(max_length=30)


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32, null=True)
    email = models.CharField(max_length=32, null=True)
    clan = models.CharField(max_length=10, choices=food_types)
    texture = models.CharField(max_length=64)
    friends = models.ManyToManyField(Friend)

