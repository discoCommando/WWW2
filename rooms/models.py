from django.db import models

class Room(models.Model):
        name = models.CharField(max_length=30)
        name.primary_key = 'true'
        capacity = models.IntegerField()
        about = models.CharField(max_length=150)

class FreeDate(models.Model):
	date = models.DateField('free date')
	room = models.ForeignKey(Room)
	from_hour = models.IntegerField() 
	to_hour = models.IntegerField()

class Booking(models.Model):
	date = models.DateField('booking date')
	room = models.ForeignKey(Room)
	from_hour = models.IntegerField()
        to_hour = models.IntegerField()
	user = models.CharField(max_length = 100)

# Create your models here.
