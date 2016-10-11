# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamer', '0002_remove_streamer_stream_uptime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='streamer',
            name='stream_online',
        ),
    ]
