# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamer', '0008_auto_20161008_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamer',
            name='streamer_avatar',
            field=models.URLField(default=b'http://google.com', max_length=300, null=True),
        ),
    ]
