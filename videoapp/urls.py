from django.conf import settings
from django.conf.urls import url

from videoapp.views import post_list, signup, post_new, post_edit, post_detail, add_comment_to_post, profile

urlpatterns = [
    url(r'^$', post_list, name = 'post_list'),
    url(r'^post/(?P<id>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', post_detail, name='post_detail'),
    url(r'^post/new/$', post_new, name='post_new'),
    url(r'^post/(?P<id>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/edit/$', post_edit, name='post_edit'),
    url(r'^post/(?P<id>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/comment/$', add_comment_to_post, name = 'add_comment_to_post'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^account/profile$', profile, name='profile'),
]
