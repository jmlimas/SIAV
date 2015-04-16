# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_cliente_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evento', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('avaluo', models.ForeignKey(to='app.Avaluo')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventoUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('leido', models.BooleanField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('envia', models.ForeignKey(related_name='enviaUsuario', to=settings.AUTH_USER_MODEL)),
                ('evento', models.ForeignKey(to='websock.Eventos')),
                ('recibe', models.ForeignKey(related_name='recibeUsuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
