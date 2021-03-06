# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

    def backwards(self, orm):
        "Write your backwards methods here."

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
    symmetrical = True
