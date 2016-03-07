from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import food_types


class ProfileUserForm(UserCreationForm):

    clan = forms.ChoiceField(choices=food_types)
    texture = forms.CharField(max_length=64)
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    email = forms.EmailField()
