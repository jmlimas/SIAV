# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('websock', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.AddField(
            model_name='comments',
            name='envia',
            field=models.ForeignKey(related_name='enviaUsuarioCmt', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='leido',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='recibe',
            field=models.ForeignKey(related_name='recibeUsuarioCmt', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
