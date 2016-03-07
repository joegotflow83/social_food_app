from django.contrib import admin

from .models import Friend, FriendList, Tag, Post


admin.site.register(Friend)
admin.site.register(FriendList)
admin.site.register(Tag)
admin.site.register(Post)
