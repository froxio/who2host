from django.db import models
from django.conf import settings


class Streamer(models.Model):
    streamer_name = models.CharField(max_length=30, default='_NONAME')
    streamer_views = models.IntegerField(default=0)
    streamer_follows = models.IntegerField(default=0)
    streamer_avatar = models.URLField(
        max_length=300, default='http://google.com', null=True)
    stream_game = models.CharField(max_length=200, default='_NOGAME')
    stream_title = models.CharField(max_length=200, default='_NOTITLE')
    stream_language = models.CharField(
        max_length=10, choices=settings.LANGUAGES, default='_NOLANG')
    stream_viewers = models.IntegerField(default=0)
    stream_thumbnail = models.URLField(
        max_length=300, default='http://google.com')
    stream_link = models.URLField(max_length=300, default='http://google.com')

    def __str__(self):
        return self.streamer_name
