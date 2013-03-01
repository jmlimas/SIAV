# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Avaluo.Valor'
        db.alter_column('app_avaluo', 'Valor', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2))

        # Changing field 'Avaluo.Gastos'
        db.alter_column('app_avaluo', 'Gastos', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2))

        # Changing field 'Avaluo.Importe'
        db.alter_column('app_avaluo', 'Importe', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2))
        # Adding field 'Valuador.is_active'
        db.add_column('app_valuador', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'Avaluo.Valor'
        db.alter_column('app_avaluo', 'Valor', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=0))

        # Changing field 'Avaluo.Gastos'
        db.alter_column('app_avaluo', 'Gastos', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Avaluo.Importe'
        db.alter_column('app_avaluo', 'Importe', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2))
        # Deleting field 'Valuador.is_active'
        db.delete_column('app_valuador', 'is_active')


    models = {
        'app.avaluo': {
            'Calle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'Cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Cliente']", 'null': 'True'}),
            'Colonia': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'Depto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Depto']", 'null': 'True'}),
            'Estado': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'Estatus': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'Factura': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'FolioK': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'Gastos': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2'}),
            'Importe': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2'}),
            'LatitudG': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '3'}),
            'LatitudM': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '3'}),
            'LatitudS': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '3'}),
            'LongitudG': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '3'}),
            'LongitudM': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '3'}),
            'LongitudS': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '3'}),
            'Mconstruccion': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2'}),
            'Meta': {'object_name': 'Avaluo'},
            'Mterreno': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2'}),
            'Municipio': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'NumExt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'NumInt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'Observaciones': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'Pagado': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Prioridad': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'Referencia': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'Salida': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'Servicio': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'Solicitud': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'Tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Tipo']", 'null': 'True'}),
            'Valor': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2'}),
            'Valuador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Valuador']", 'null': 'True'}),
            'Visita': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'avaluo_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'app.cliente': {
            'Cliente': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Meta': {'object_name': 'Cliente'},
            'cliente_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'app.depto': {
            'CP': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Calle': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Ciudad': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'Colonia': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Depto': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Digitos': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'Meta': {'object_name': 'Depto'},
            'Metodo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'RFC': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Razon': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Tolerancia': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cliente_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Cliente']"}),
            'depto_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'app.estado': {
            'Meta': {'object_name': 'Estado'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'estado_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'app.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'estado_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Estado']"}),
            'municipio_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'app.tipo': {
            'Meta': {'object_name': 'Tipo'},
            'Tipo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipo_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'app.valuador': {
            'Apellido': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'Correo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'Meta': {'object_name': 'Valuador'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'valuador_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['app']