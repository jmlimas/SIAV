# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Investigacion_Mercado.ficha_id'
        db.add_column('ficha_investigacion_mercado', 'ficha_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['ficha.Ficha_Tecnica']),
                      keep_default=False)

        # Removing M2M table for field investigacion_mercado on 'Ficha_Tecnica'
        db.delete_table('ficha_ficha_tecnica_investigacion_mercado')


    def backwards(self, orm):
        # Deleting field 'Investigacion_Mercado.ficha_id'
        db.delete_column('ficha_investigacion_mercado', 'ficha_id_id')

        # Adding M2M table for field investigacion_mercado on 'Ficha_Tecnica'
        db.create_table('ficha_ficha_tecnica_investigacion_mercado', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ficha_tecnica', models.ForeignKey(orm['ficha.ficha_tecnica'], null=False)),
            ('investigacion_mercado', models.ForeignKey(orm['ficha.investigacion_mercado'], null=False))
        ))
        db.create_unique('ficha_ficha_tecnica_investigacion_mercado', ['ficha_tecnica_id', 'investigacion_mercado_id'])


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
            'ficha_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ficha.Ficha_Tecnica']"}),
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