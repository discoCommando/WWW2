from django.db import models
from django.db.models import Q	

class Attribute(models.Model):
        name = models.CharField(max_length=30)
        def __unicode__(self):
                return self.name; 

class Room(models.Model):
        name = models.CharField(max_length=30)
        name.primary_key = 'true'
        capacity = models.IntegerField()
        about = models.CharField(max_length=150)
        attribute = models.ManyToManyField(Attribute)
        def __unicode__(self):
                return self.name;
                
       

class FreeDate(models.Model):
	date = models.DateField('free date')
	room = models.ForeignKey(Room)
	from_hour = models.IntegerField() 
	to_hour = models.IntegerField()
	
	def __unicode__(self):
		return self.room.name + " " + str(self.from_hour) + "-" + str(self.to_hour) + " " + str(self.date);
	
	def save(self, force_insert=False, force_update=False, using=None):
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
						
		fd_from = Booking.objects.all().filter(Q(date = self.date) & Q(room = self.room) & Q(from_hour__lte = self.from_hour) & Q(to_hour__gt = self.from_hour))
		fd_to = Booking.objects.all().filter(Q(date = self.date) & Q(room = self.room) & Q(from_hour__lt = self.to_hour) & Q(to_hour__gte = self.to_hour))
		fd_from_to_bigger = Booking.objects.all().filter(Q(date = self.date) & Q(room = self.room) & Q(from_hour__gte = self.from_hour) & Q(to_hour__lte = self.to_hour))
		fd_from_to_smaller = Booking.objects.all().filter(Q(date = self.date) & Q(room = self.room) & Q(from_hour__lte = self.from_hour) & Q(to_hour__gte = self.to_hour))
		
		can_save2 = False
		if not fd_from:
			if not fd_to:
				if not fd_from_to_bigger:
					if not fd_from_to_smaller:
						can_save2 = True
		
		same_date = FreeDate.objects.all().filter(Q(date = self.date))
		ts_fr = same_date.filter(Q(from_hour = self.to_hour))
		ts_t = same_date.filter(Q(to_hour = self.from_hour))
		
		if self.to_hour <= self.from_hour:
			can_save = False
		
		if can_save & can_save2:
			if ts_fr:
				self.to_hour = ts_fr.first().to_hour;
				ts_fr.first().delete()
			if ts_t:
				self.from_hour = ts_t.first().from_hour;
				ts_t.first().delete()
			
			models.Model.save(self, force_insert, force_update, using)
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
		
		
	def save(self, force_insert=False, force_update=False, using=None):
		room = FreeDate.objects.all().filter(Q(room = self.room) & Q(date = self.date) & Q(from_hour__lte = self.from_hour) & Q(to_hour__gte = self.to_hour))
   
		if not room:
			raise Exception('Zajety pokoj')
		else:
			roomz = room.first()
			room.first().delete()
			if roomz.from_hour < self.from_hour:
				try:
					FreeDate.objects.create(date = roomz.date, room = roomz.room, from_hour = roomz.from_hour, to_hour = self.from_hour)
				except Exception:
					roomz = roomz
			if roomz.to_hour > self.to_hour:
				try:
					FreeDate.objects.create(date = roomz.date, room = roomz.room, from_hour = self.to_hour, to_hour = roomz.to_hour)
				except Exception:
					roomz = roomz
			models.Model.save(self, force_insert, force_update, using)
		
# Create your models here.
