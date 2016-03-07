from django.db import models
from django.contrib.auth.models import User


food_types = (
    ('Fruit', 'Fruit'),
    ('Vegetable', 'Vegetable')
)


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    clan = models.CharField(max_length=10, choices=food_types)
    texture = models.CharField(max_length=64)

