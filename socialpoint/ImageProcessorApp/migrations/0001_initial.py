# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.IntegerField(choices=[(1, 'uploaded'), (2, 'processing'), (3, 'finished')], default=1)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-uploaded'],
                'db_table': 'tasks',
                'verbose_name_plural': 'tasks',
            },
        ),
    ]
