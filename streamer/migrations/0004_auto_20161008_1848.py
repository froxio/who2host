# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamer', '0003_remove_streamer_stream_online'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamer',
            name='streamer_name',
            field=models.CharField(default=b'_NONAME', max_length=30),
        ),
    ]
