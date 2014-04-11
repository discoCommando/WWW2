from django.test import TestCase
from django.db.models import Q	

# Create your tests here.

	def setUp(self):
		Room.objects.create(name="Test", capacity=666, about="Over 9000")
		FreeDates.objects.create(date="11.04.2014", room="Test", from_hour=0, to_hour=12)
		Booking.objects.create(date="11.04.2014", room="Test", from_hour=12, to_hour=23, user="disco")
	
	def check_add_room(self):
		t1 = Room.objects.all().filter(Q(name="Test"))
		t2 = Room.objects.all().filter(Q(name="Test") | Q(capacity=666))
		t3 = Room.objects.all().filter(Q(name="Test") | Q(capacity=666) | Q(about="Over 9000"))
		self.assertTrue(t1)
		self.assertTrue(t2)
		self.assertTrue(t3)
		
	def check_add_free_dates(self):
		t1 = FreeDates.objects.all().filter(Q(date="11.04.2014"))
		t2 = FreeDates.objects.all().filter(Q(date="11.04.2014") | Q(room="Test"))
		t3 = FreeDates.objects.all().filter(Q(date="11.04.2014") | Q(room="Test") | Q(from_hour=0))
		t4 = FreeDates.objects.all().filter(Q(date="11.04.2014") | Q(room="Test") | Q(from_hour=0) | Q(to_hour=12))
		self.assertTrue(t1)
		self.assertTrue(t2)
		self.assertTrue(t3)
		self.assertTrue(t4)
		
	def check_add_room_booking(self):
		t1 = FreeDates.objects.all().filter(Q(date="11.04.2014"))
		t2 = FreeDates.objects.all().filter(Q(date="11.04.2014") | Q(room="Test"))
		t3 = FreeDates.objects.all().filter(Q(date="11.04.2014") | Q(room="Test") | Q(from_hour=12))
		t4 = FreeDates.objects.all().filter(Q(date="11.04.2014") | Q(room="Test") | Q(from_hour=12) | Q(to_hour=24))
		t5 = FreeDates.objects.all().filter(Q(date="11.04.2014") | Q(room="Test") | Q(from_hour=12) | Q(to_hour=24) | Q(user="disco"))
		self.assertTrue(t1)
		self.assertTrue(t2)
		self.assertTrue(t3)
		self.assertTrue(t4)
		self.assertTrue(t5)
		
	
	def check_add_free_dates_incorrectly(self):
		FreeDates.objects.create(date="11.04.2014", room="Test", from_hour=1, to_hour=12)
		t1 = FreeDates.objects.all().filter(Q(date="11.04.2014") | Q(room="Test") | Q(from_hour=1) | Q(to_hour=12))
		self.assertTrue(not t1)
		
		
