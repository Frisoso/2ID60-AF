from __future__ import unicode_literals

import uuid
from django.db import models
from django.utils import timezone
from videokit.models import VideoField, VideoSpecField
from videosite.storage_backends import CacheMediaStorage, PublicMediaStorage

# Create your models here.
def upload_to(instance, filename):
    return 'media_items/%s' % filename

class Post(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    video = VideoField( upload_to = upload_to,
                        null = True, blank = True, default = None,
                        storage = PublicMediaStorage() )
    video_cache = VideoField( upload_to = upload_to,
                        width_field = 'video_width', height_field = 'video_height',
                        rotation_field = 'video_rotation',
                        mimetype_field = 'video_mimetype',
                        duration_field = 'video_duration',
                        thumbnail_field = 'video_thumbnail',
                        storage = CacheMediaStorage())
    video_width = models.IntegerField(null = True, blank = True)
    video_height = models.IntegerField(null = True, blank = True)
    video_rotation = models.FloatField(null = True, blank = True)
    video_mimetype = models.CharField(max_length = 32, null = True, blank = True)
    video_duration = models.IntegerField(null = True, blank = True)
    video_thumbnail = models.ImageField(null = True, blank = True)

    #video_mp4 = VideoSpecField(source = 'video', format = 'mp4')
    #video_ogg = VideoSpecField(source = 'video', format = 'ogg')

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, default='SampleTitle')
    description = models.TextField(default='SampleDescription')
    upload_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    def publish(self):
        self.publish_date = timezone.now()
        self.published = True
        self.save()

    def comments(self):
        return self.comments()

    def __unicode__(self):
        return self.video.name

    def video_specs_generated(self):
        if self.video_mp4.generated() and self.video_ogg.generated():
            return True

        return False

    def delete_cache(self):
        storage, path = self.video_cache.storage, self.video_cache.path
        storage.delete(path)

class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments')
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.text
