# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0005_line'),
    ]

    operations = [
        migrations.CreateModel(
            name='NowPlay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('table', models.IntegerField()),
                ('song', models.ForeignKey(to='Orders.Song')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
