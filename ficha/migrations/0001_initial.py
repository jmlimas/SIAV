# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Investigacion_Mercado'
        db.create_table('ficha_investigacion_mercado', (
            ('investigacion_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('calle', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('colonia', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('fuente', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('uso', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('m_terreno', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('m_construccion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('oferta', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2)),
            ('unitario', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2)),
        ))
        db.send_create_signal('ficha', ['Investigacion_Mercado'])

        # Adding model 'Ficha_Tecnica'
        db.create_table('ficha_ficha_tecnica', (
            ('folio', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('region', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('colonia', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('lote_tipo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('valuador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('limite_norte', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('limite_sur', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('limite_oriente', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('limite_poniente', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('servicio_1', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('servicio_2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('servicio_3', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('condicion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('equipamiento', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('uso_suelo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('socioeconomico', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('calidad', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('niveles', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('densidad', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('entorno_urbano_1', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('entorno_urbano_2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('riesgo_1', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('riesgo_2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('valor_propuesto', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal('ficha', ['Ficha_Tecnica'])

        # Adding M2M table for field investigacion_mercado on 'Ficha_Tecnica'
        m2m_table_name = db.shorten_name('ficha_ficha_tecnica_investigacion_mercado')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ficha_tecnica', models.ForeignKey(orm['ficha.ficha_tecnica'], null=False)),
            ('investigacion_mercado', models.ForeignKey(orm['ficha.investigacion_mercado'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ficha_tecnica_id', 'investigacion_mercado_id'])

        # Adding model 'ImagenFicha'
        db.create_table('ficha_imagenficha', (
            ('imagen_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('folio', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha.Ficha_Tecnica'])),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('ficha', ['ImagenFicha'])

        # Adding model 'ArchivoFicha'
        db.create_table('ficha_archivoficha', (
            ('archivo_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('folio', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ficha.Ficha_Tecnica'])),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('ficha', ['ArchivoFicha'])


    def backwards(self, orm):
        # Deleting model 'Investigacion_Mercado'
        db.delete_table('ficha_investigacion_mercado')

        # Deleting model 'Ficha_Tecnica'
        db.delete_table('ficha_ficha_tecnica')

        # Removing M2M table for field investigacion_mercado on 'Ficha_Tecnica'
        db.delete_table(db.shorten_name('ficha_ficha_tecnica_investigacion_mercado'))

        # Deleting model 'ImagenFicha'
        db.delete_table('ficha_imagenficha')

        # Deleting model 'ArchivoFicha'
        db.delete_table('ficha_archivoficha')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'ficha.archivoficha': {
            'Meta': {'object_name': 'ArchivoFicha'},
            'archivo_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ficha.Ficha_Tecnica']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'folio': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'ficha.ficha_tecnica': {
            'Meta': {'object_name': 'Ficha_Tecnica'},
            'calidad': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'condicion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'densidad': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'entorno_urbano_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'entorno_urbano_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'equipamiento': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'folio': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'investigacion_mercado': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ficha.Investigacion_Mercado']", 'symmetrical': 'False'}),
            'limite_norte': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'limite_oriente': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'limite_poniente': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'limite_sur': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'lote_tipo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'niveles': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'region': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'riesgo_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'riesgo_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'servicio_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'servicio_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'servicio_3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'socioeconomico': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'uso_suelo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'valor_propuesto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'valuador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        },
        'ficha.imagenficha': {
            'Meta': {'object_name': 'ImagenFicha'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ficha.Ficha_Tecnica']"}),
            'folio': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'imagen_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'ficha.investigacion_mercado': {
            'Meta': {'object_name': 'Investigacion_Mercado'},
            'calle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'fuente': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'investigacion_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_construccion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'm_terreno': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'oferta': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'unitario': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2'}),
            'uso': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        }
    }

    complete_apps = ['ficha']