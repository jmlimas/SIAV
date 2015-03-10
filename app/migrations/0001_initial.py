# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import app.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivoAvaluo',
            fields=[
                ('archivo_id', models.AutoField(serialize=False, primary_key=True)),
                ('FolioK', models.CharField(max_length=255, null=True)),
                ('file', models.FileField(upload_to=app.models.get_image_path, null=True, verbose_name=b'Archivo Avaluo', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Avaluo',
            fields=[
                ('avaluo_id', models.AutoField(serialize=False, primary_key=True)),
                ('Referencia', models.CharField(max_length=255, unique=True, null=True)),
                ('FolioK', models.CharField(max_length=255, unique=True, null=True)),
                ('Calle', models.CharField(max_length=255, null=True)),
                ('NumExt', models.CharField(max_length=255, null=True)),
                ('NumInt', models.CharField(max_length=255, null=True)),
                ('Colonia', models.CharField(max_length=255, null=True)),
                ('Servicio', models.CharField(max_length=255, null=True)),
                ('Estatus', models.CharField(max_length=255, null=True)),
                ('Prioridad', models.CharField(max_length=255, null=True)),
                ('Solicitud', models.DateField(null=True)),
                ('Mterreno', models.DecimalField(null=True, max_digits=12, decimal_places=2)),
                ('Mconstruccion', models.DecimalField(null=True, max_digits=12, decimal_places=2)),
                ('LatitudG', models.DecimalField(null=True, max_digits=12, decimal_places=3)),
                ('LatitudM', models.DecimalField(null=True, max_digits=12, decimal_places=3)),
                ('LatitudS', models.DecimalField(null=True, max_digits=12, decimal_places=3)),
                ('LongitudG', models.DecimalField(null=True, max_digits=12, decimal_places=3)),
                ('LongitudM', models.DecimalField(null=True, max_digits=12, decimal_places=3)),
                ('LongitudS', models.DecimalField(null=True, max_digits=12, decimal_places=3)),
                ('Declat', models.DecimalField(null=True, max_digits=12, decimal_places=5)),
                ('Declon', models.DecimalField(null=True, max_digits=12, decimal_places=5)),
                ('Visita', models.DateField(null=True)),
                ('Valor', models.DecimalField(default=Decimal('0'), null=True, max_digits=15, decimal_places=2, blank=True)),
                ('Gastos', models.DecimalField(null=True, max_digits=15, decimal_places=2)),
                ('Importe', models.DecimalField(null=True, max_digits=15, decimal_places=2)),
                ('Salida', models.DateField(null=True)),
                ('Factura', models.CharField(max_length=30, null=True)),
                ('Pagado', models.NullBooleanField()),
                ('Observaciones', models.CharField(max_length=255, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.AutoField(serialize=False, primary_key=True)),
                ('Cliente', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Depto',
            fields=[
                ('depto_id', models.AutoField(serialize=False, primary_key=True)),
                ('is_active', models.BooleanField()),
                ('Depto', models.CharField(max_length=255)),
                ('Razon', models.CharField(max_length=255)),
                ('RFC', models.CharField(max_length=255)),
                ('Calle', models.CharField(max_length=255)),
                ('Colonia', models.CharField(max_length=255)),
                ('CP', models.CharField(max_length=255)),
                ('Ciudad', models.CharField(max_length=150)),
                ('Metodo', models.CharField(max_length=50, null=True)),
                ('Digitos', models.CharField(max_length=15, null=True)),
                ('Tolerancia', models.CharField(max_length=255)),
                ('base', models.DecimalField(null=True, max_digits=15, decimal_places=2)),
                ('factor', models.DecimalField(null=True, max_digits=6, decimal_places=3)),
                ('cliente_id', models.ForeignKey(to='app.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('estado_id', models.AutoField(serialize=False, primary_key=True)),
                ('clave', models.CharField(max_length=255, null=True)),
                ('Nombre', models.CharField(max_length=255)),
                ('abrev', models.CharField(max_length=255, null=True)),
                ('is_active', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImagenAvaluo',
            fields=[
                ('imagen_id', models.AutoField(serialize=False, primary_key=True)),
                ('FolioK', models.CharField(max_length=255, null=True)),
                ('imagen', models.ImageField(upload_to=app.models.get_image_path, null=True, verbose_name=b'Imagen Avaluo', blank=True)),
                ('avaluo', models.ForeignKey(related_name='avaluos', to='app.Avaluo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('municipio_id', models.AutoField(serialize=False, primary_key=True)),
                ('clave', models.CharField(max_length=255, null=True)),
                ('Nombre', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=1)),
                ('estado_id', models.ForeignKey(to='app.Estado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('tipo_id', models.AutoField(serialize=False, primary_key=True)),
                ('Tipo', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(upload_to=app.models.get_image_path, blank=True)),
                ('color', models.CharField(max_length=50, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Valuador',
            fields=[
                ('valuador_id', models.AutoField(serialize=False, primary_key=True)),
                ('Nombre', models.CharField(max_length=255, null=True)),
                ('Apellido', models.CharField(max_length=255, null=True)),
                ('Correo', models.CharField(max_length=255, null=True)),
                ('is_active', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='avaluo',
            name='Cliente',
            field=models.ForeignKey(to='app.Cliente', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avaluo',
            name='Depto',
            field=models.ForeignKey(to='app.Depto', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avaluo',
            name='Estado',
            field=models.ForeignKey(to='app.Estado', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avaluo',
            name='Municipio',
            field=models.ForeignKey(to='app.Municipio', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avaluo',
            name='Tipo',
            field=models.ForeignKey(to='app.Tipo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avaluo',
            name='Valuador',
            field=models.ForeignKey(to='app.Valuador', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='archivoavaluo',
            name='avaluo',
            field=models.ForeignKey(to='app.Avaluo'),
            preserve_default=True,
        ),
    ]
