from django.conf.urls import url

from blog import views


urlpatterns = [
    url(r'^blog/$', views.Blog.as_view(), name='blog'),
    url(r'^create_post/$', views.CreatePost.as_view(), name='create_post'),
    url(r'^users/$', views.UserList.as_view(), name='user_list'),
]
