# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tittle', models.CharField(max_length=50)),
                ('minus_quality', models.IntegerField()),
                ('back_vocal', models.IntegerField()),
                ('karaoke_system', models.CharField(max_length=30)),
                ('artist', models.ForeignKey(to='Orders.Artist')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
