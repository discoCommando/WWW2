# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Room'
        db.create_table(u'rooms_room', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key='true')),
            ('capacity', self.gf('django.db.models.fields.IntegerField')()),
            ('about', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'rooms', ['Room'])

        # Adding model 'FreeDate'
        db.create_table(u'rooms_freedate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rooms.Room'])),
            ('from_hour', self.gf('django.db.models.fields.IntegerField')()),
            ('to_hour', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'rooms', ['FreeDate'])

        # Adding model 'Booking'
        db.create_table(u'rooms_booking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rooms.Room'])),
            ('from_hour', self.gf('django.db.models.fields.IntegerField')()),
            ('to_hour', self.gf('django.db.models.fields.IntegerField')()),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'rooms', ['Booking'])


    def backwards(self, orm):
        # Deleting model 'Room'
        db.delete_table(u'rooms_room')

        # Deleting model 'FreeDate'
        db.delete_table(u'rooms_freedate')

        # Deleting model 'Booking'
        db.delete_table(u'rooms_booking')


    models = {
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
            'capacity': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': "'true'"})
        }
    }

    complete_apps = ['rooms']