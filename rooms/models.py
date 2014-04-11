from django.db import models
from django.db.models import Q	

class Room(models.Model):
        name = models.CharField(max_length=30)
        name.primary_key = 'true'
        capacity = models.IntegerField()
        about = models.CharField(max_length=150)
        
        def __unicode__(self):
                return self.name;  

class FreeDate(models.Model):
	date = models.DateField('free date')
	room = models.ForeignKey(Room)
	from_hour = models.IntegerField() 
	to_hour = models.IntegerField()
	
	def __unicode__(self):
		return self.room.name;
	
	def save(self, force_insert=False, force_update=False):
		fd_from = FreeDate.objects.all().filter(Q(date = self.date) & Q(room = self.room) & Q(from_hour__lte = self.from_hour) & Q(to_hour__gt = self.from_hour))
		fd_to = FreeDate.objects.all().filter(Q(date = self.date) & Q(room = self.room) & Q(from_hour__lt = self.to_hour) & Q(to_hour__gte = self.to_hour))
		fd_from_to_bigger = FreeDate.objects.all().filter(Q(date = self.date) & Q(room = self.room) & Q(from_hour__gte = self.from_hour) & Q(to_hour__lte = self.to_hour))
		fd_from_to_smaller = FreeDate.objects.all().filter(Q(date = self.date) & Q(room = self.room) & Q(from_hour__lte = self.from_hour) & Q(to_hour__gte = self.to_hour))
		can_save = False
		if not fd_from:
			if not fd_to:
				if not fd_from_to_bigger:
					if not fd_from_to_smaller:
						can_save = True
						
		if can_save:
			models.Model.save(self, force_insert, force_update)
		else:
			raise Exception('Nieprawidlowe wartosci')

class Booking(models.Model):
	date = models.DateField('booking date')
	room = models.ForeignKey(Room)
	from_hour = models.IntegerField()
        to_hour = models.IntegerField()
	user = models.CharField(max_length = 100)
	
	def __unicode__(self):
		return self.room.name;

# Create your models here.
