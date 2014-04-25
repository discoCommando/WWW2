from django.test import TestCase
from django.db.models import Q
from models import Room, FreeDate, Booking

# Create your tests here.
class QuestionMethodTests(TestCase):
	def setUp(self):
		pass

	def test_check_add_room(self):
		t1 = Room.objects.all().filter(Q(name="Test"))
		t2 = Room.objects.all().filter(Q(name="Test") & Q(capacity=666))
		t3 = Room.objects.all().filter(Q(name="Test") & Q(capacity=666) & Q(about="Over 9000"))
		self.assertTrue(t1)
		self.assertTrue(t2)
		self.assertTrue(t3)
		
	def test_check_add_free_dates(self):
		room_ = Room.objects.all().filter(Q(name="Test")).first()
		t1 = FreeDate.objects.all().filter(Q(date="2014-04-11"))
		t2 = FreeDate.objects.all().filter(Q(date="2014-04-11") & Q(room=room_))
		t3 = FreeDate.objects.all().filter(Q(date="2014-04-11") & Q(room=room_) & Q(from_hour=0))
		t4 = FreeDate.objects.all().filter(Q(date="2014-04-11") & Q(room=room_) & Q(from_hour=0) & Q(to_hour=12))
		self.assertTrue(t1)
		self.assertTrue(t2)
		self.assertTrue(t3)
		self.assertTrue(t4)
		
	def test_check_add_room_booking(self):
		room_ = Room.objects.all().filter(Q(name="Test")).first()
		t1 = Booking.objects.all().filter(Q(date="2014-04-11"))
		t2 = Booking.objects.all().filter(Q(date="2014-04-11") & Q(room=room_))
		t3 = Booking.objects.all().filter(Q(date="2014-04-11") & Q(room=room_) & Q(from_hour=12))
		t4 = Booking.objects.all().filter(Q(date="2014-04-11") & Q(room=room_) & Q(from_hour=12) & Q(to_hour=23))
		t5 = Booking.objects.all().filter(Q(date="2014-04-11") & Q(room=room_) & Q(from_hour=12) & Q(to_hour=23) & Q(user="disco"))
		self.assertTrue(t1)
		self.assertTrue(t2)
		self.assertTrue(t3)
		self.assertTrue(t4)
		self.assertTrue(t5)
		
	def test_add_incorrect_free_date(self):
		try:
			FreeDate.objects.create(Q(date="2014-04-11") & Q(room=room_) & Q(from_hour=10) & Q(to_hour=11))
			self.assertTrue(False)
		except Exception:
			self.assertTrue(True)
			
			
	def test_add_booked_free_date(self):
		try:
			FreeDate.objects.create(Q(date="2014-04-11") & Q(room=room_) & Q(from_hour=12) & Q(to_hour=14))
			self.assertTrue(False)
		except Exception:
			self.assertTrue(True)
		

		
		
