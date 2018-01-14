from django.conf import settings
from django.conf.urls import url

from videoapp.views import list
from videoapp.views import item_create

urlpatterns = [
    url(r'^$', list, name = 'list'),
    url(r'^item_create/', item_create, name = 'item_create'),
]
