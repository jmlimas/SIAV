# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Estado'
        db.create_table('app_estado', (
            ('estado_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('app', ['Estado'])

        # Adding model 'Municipio'
        db.create_table('app_municipio', (
            ('municipio_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Estado'])),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('app', ['Municipio'])

        # Adding model 'Valuador'
        db.create_table('app_valuador', (
            ('valuador_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('Apellido', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('Correo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal('app', ['Valuador'])

        # Adding model 'Cliente'
        db.create_table('app_cliente', (
            ('cliente_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Cliente', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('app', ['Cliente'])

        # Adding model 'Tipo'
        db.create_table('app_tipo', (
            ('tipo_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Tipo', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('app', ['Tipo'])

        # Adding model 'Depto'
        db.create_table('app_depto', (
            ('depto_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Cliente'])),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Depto', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('Razon', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('RFC', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('Calle', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('Colonia', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('CP', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('Ciudad', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('Metodo', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('Digitos', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('Tolerancia', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('app', ['Depto'])

        # Adding model 'Avaluo'
        db.create_table('app_avaluo', (
            ('avaluo_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Referencia', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('FolioK', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('Calle', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('NumExt', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('NumInt', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('Colonia', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('Municipio', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('Estado', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('Servicio', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('Tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Tipo'], null=True)),
            ('Estatus', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('Prioridad', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('Cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Cliente'], null=True)),
            ('Depto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Depto'], null=True)),
            ('Valuador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Valuador'], null=True)),
            ('Solicitud', self.gf('django.db.models.fields.DateField')(null=True)),
            ('Mterreno', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2)),
            ('Mconstruccion', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2)),
            ('LatitudG', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=3)),
            ('LatitudM', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=3)),
            ('LatitudS', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=3)),
            ('LongitudG', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=3)),
            ('LongitudM', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=3)),
            ('LongitudS', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=3)),
            ('Visita', self.gf('django.db.models.fields.DateField')(null=True)),
            ('Valor', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=0)),
            ('Gastos', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2)),
            ('Importe', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2)),
            ('Salida', self.gf('django.db.models.fields.DateField')(null=True)),
            ('Factura', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('Pagado', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('Observaciones', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal('app', ['Avaluo'])


    def backwards(self, orm):
        # Deleting model 'Estado'
        db.delete_table('app_estado')

        # Deleting model 'Municipio'
        db.delete_table('app_municipio')

        # Deleting model 'Valuador'
        db.delete_table('app_valuador')

        # Deleting model 'Cliente'
        db.delete_table('app_cliente')

        # Deleting model 'Tipo'
        db.delete_table('app_tipo')

        # Deleting model 'Depto'
        db.delete_table('app_depto')

        # Deleting model 'Avaluo'
        db.delete_table('app_avaluo')


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
            'Gastos': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'Importe': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2'}),
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
            'Valor': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '0'}),
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
            'valuador_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['app']