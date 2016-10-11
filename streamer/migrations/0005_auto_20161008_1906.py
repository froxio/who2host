# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamer', '0004_auto_20161008_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='streamer',
            name='stream_game',
        ),
        migrations.RemoveField(
            model_name='streamer',
            name='stream_language',
        ),
        migrations.RemoveField(
            model_name='streamer',
            name='stream_link',
        ),
        migrations.RemoveField(
            model_name='streamer',
            name='stream_thumbnail',
        ),
        migrations.RemoveField(
            model_name='streamer',
            name='stream_title',
        ),
        migrations.RemoveField(
            model_name='streamer',
            name='stream_viewers',
        ),
        migrations.RemoveField(
            model_name='streamer',
            name='streamer_avatar',
        ),
        migrations.RemoveField(
            model_name='streamer',
            name='streamer_follows',
        ),
        migrations.RemoveField(
            model_name='streamer',
            name='streamer_views',
        ),
    ]
