# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0003_song_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='back_vocal',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='song',
            name='minus_quality',
            field=models.CharField(max_length=30),
        ),
    ]
