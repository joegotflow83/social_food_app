from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .models import Post


class Blog(ListView):
    """Display the users blogs"""
    model = Post

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

class CreatePost(CreateView):
    """Allow a user to create a post"""
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        """Validate the form"""
        post_object = form.save(commit=False)
        post_object.user = self.request.user
        post_object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog')


class UserList(ListView):
    """Display all active users on the site"""
    model = User
