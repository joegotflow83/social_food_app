from django.conf.urls import url

from blog import views


urlpatterns = [
    url(r'^blog/$', views.Blog.as_view(), name='blog'),
    url(r'^create_post/$', views.CreatePost.as_view(), name='create_post'),
    url(r'^users/$', views.UserList.as_view(), name='user_list'),
    url(r'^add_friend/(?P<pk>\d+)/$',  views.AddFriend.as_view(), name='add_friend'),
    url(r'^friends_list/$', views.FriendsList.as_view(), name='friends_list'),
    url(r'^friends_posts/(?P<pk>\d+)/$', views.FriendDetail.as_view(), name='friends_detail'),
    url(r'^forum/$', views.Forum.as_view(), name='forum'),
    url(r'^forum_post/$', views.ForumPost.as_view(), name='forum_post'),
    url(r'^$', views.Index.as_view(), name='index'),
]
