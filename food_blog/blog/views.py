from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .models import Post
from accounts.models import UserProfile
from accounts.models import Friend


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


class AddFriend(View):
    """Add a new friend"""
    def get(self, request, pk):
        new_friend = User.objects.get(pk=pk)
        new_friend_name = Friend(username=new_friend.username)
        user_profile = self.request.user.userprofile
        new_friend_name.save()
        user_profile.friends.add(new_friend_name)
        user_profile.save()
        return render(request, 'blog/add_friend.html')


class FriendsList(View):
    """Display all users the current user is following"""
    def get(self, request):
        user = User.objects.get(pk=request.user.id)
        all_friends = user.userprofile.friends.all()
        return render(request, 'accounts/friends_list.html', {'friends': all_friends})


class FriendDetail(ListView):
    """View a friends posts"""
    model = User
    template_name = 'accounts/userprofile_list.html'

    def get_queryset(self):
        return self.model.objects.filter(pk=self.kwargs['pk'])
