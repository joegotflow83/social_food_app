from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

from .models import UserProfile
from .forms import ProfileUserForm


class Signup(CreateView):
    """Allow a user to create an account"""
    model = User
    form_class = ProfileUserForm

    def form_valid(self, form):
        """Validate the form and create the user profile"""
        user_object = form.save()
        UserProfile.objects.create(user=user_object,
                                   clan=form.cleaned_data['clan'],
                                   texture=form.cleaned_data['texture'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')
