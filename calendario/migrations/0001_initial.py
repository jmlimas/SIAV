# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('evento_id', models.AutoField(serialize=False, primary_key=True)),
                ('Inicio', models.DateField(null=True, blank=True)),
                ('Fin', models.DateField(null=True, blank=True)),
                ('diaEntero', models.NullBooleanField()),
                ('asigna', models.ForeignKey(related_name='evento_asignacion_created', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('avaluo', models.ForeignKey(blank=True, to='app.Avaluo', null=True)),
                ('visita', models.ForeignKey(related_name='evento_visita_created', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
