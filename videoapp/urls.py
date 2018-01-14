from django.conf import settings
from django.conf.urls import url

from videoapp.views import list, post_list, signup, post_new, post_edit, post_detail, add_comment_to_post
from videoapp.views import item_create

urlpatterns = [
    url(r'^$', post_list, name = 'post_list'),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^post/new/$', post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/comment/$', add_comment_to_post, name = 'add_comment_to_post'),
    url(r'^signup/$', signup, name='signup'),
]
