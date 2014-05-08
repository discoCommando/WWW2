# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Attribute'
        db.create_table(u'rooms_attribute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'rooms', ['Attribute'])

        # Adding M2M table for field attribute on 'Room'
        m2m_table_name = db.shorten_name(u'rooms_room_attribute')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('room', models.ForeignKey(orm[u'rooms.room'], null=False)),
            ('attribute', models.ForeignKey(orm[u'rooms.attribute'], null=False))
        ))
        db.create_unique(m2m_table_name, ['room_id', 'attribute_id'])


    def backwards(self, orm):
        # Deleting model 'Attribute'
        db.delete_table(u'rooms_attribute')

        # Removing M2M table for field attribute on 'Room'
        db.delete_table(db.shorten_name(u'rooms_room_attribute'))


    models = {
        u'rooms.attribute': {
            'Meta': {'object_name': 'Attribute'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'rooms.booking': {
            'Meta': {'object_name': 'Booking'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'from_hour': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rooms.Room']"}),
            'to_hour': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'rooms.freedate': {
            'Meta': {'object_name': 'FreeDate'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'from_hour': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rooms.Room']"}),
            'to_hour': ('django.db.models.fields.IntegerField', [], {})
        },
        u'rooms.room': {
            'Meta': {'object_name': 'Room'},
            'about': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'attribute': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['rooms.Attribute']", 'symmetrical': 'False'}),
            'capacity': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': "'true'"})
        }
    }

    complete_apps = ['rooms']