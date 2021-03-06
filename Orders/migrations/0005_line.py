# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0004_auto_20141016_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('table', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('song', models.ForeignKey(to='Orders.Song')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
