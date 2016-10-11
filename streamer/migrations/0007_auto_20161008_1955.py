# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamer', '0006_auto_20161008_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamer',
            name='stream_thumbnail',
            field=models.URLField(default=b'http://google.com', max_length=300),
        ),
        migrations.AlterField(
            model_name='streamer',
            name='streamer_avatar',
            field=models.ImageField(default=b'http://google.com', max_length=300, upload_to=b''),
        ),
    ]
