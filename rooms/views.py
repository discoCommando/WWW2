from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import FieldError, ValidationError
from django.db.models import Q
from django.db import transaction
from models import Room, FreeDate, Booking


def main(request):
    return render(request, 'main.html')


def logout_(request):
    logout(request)
    return redirect('main')

def login_(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            messages.error(request, 'Konto zablokowane')
    else:
        messages.error(request, 'Zle haslo')
    return redirect('main')
    
    
def search(request):

   phrase = request.POST['phrase']
   return  room_list(request, phrase)
   
   
   
   
   
def booking(request):
   name = request.GET.get('name')
   return render(request, 'booking.html', {"name": name})

def final_decision(request):
   name = request.POST['name']
   date = request.POST['date']
   from_hour = request.POST['from_hour']
   to_hour = request.POST['to_hour']
   return render(request, 'final_decision.html', {"name": name, "date": date, "from_hour": from_hour, "to_hour": to_hour})
   
@transaction.atomic  
def actual_booking(request):
  name_ = request.POST['name']
  date_ = request.POST['date']
  from_hour_ = int(request.POST['from_hour'])
  to_hour_ = int(request.POST['to_hour'])
  
  
  if from_hour_ >= to_hour_:
    message = "Godzina Od jest wieksza rowna od godziny Do"
    return render(request, 'failure.html', {"message": message})  
   
  try:
    room = FreeDate.objects.all().filter(Q(room = name_) & Q(date = date_) & Q(from_hour__lte = from_hour_) & Q(to_hour__gte = to_hour_))
  except ValidationError:
    message = "Nie znaleziono wolnego terminu"
    return render(request, 'failure.html', {"message": message})
   
  if not room:
    message = "Nie znaleziono wolnego terminu"
    return render(request, 'failure.html', {"message": message})
  else:
    if room.first().from_hour < from_hour_:
      FreeDate.objects.create(date = room.first().date, room = room.first().room, from_hour = room.first().from_hour, to_hour = from_hour_)
    if room.first().to_hour > to_hour_:
      FreeDate.objects.create(date = room.first().date, room = room.first().room, from_hour = to_hour_, to_hour = room.first().to_hour)
    Booking.objects.create(date = room.first().date, room = room.first().room, from_hour = from_hour_, to_hour = to_hour_, user = request.user)
    room.first().delete()
        
    return render(request, 'success.html')
   
def room_list(request):
    
    
    
        
        sort = request.GET.get('sort')
        
        if not sort:
                room_list = Room.objects.all()
        elif sort == "name":
                room_list = Room.objects.all().order_by(sort)
        elif sort == "capacity":
                room_list = Room.objects.all().order_by(sort)
        else: 
                room_list = Room.objects.all()
               
         


        phrase = request.GET.get('phrase')
        if phrase:
                try:
                        room_list = room_list.filter(Q(name__contains = phrase) | Q(capacity = phrase) | Q(about__contains = phrase))
                except ValueError:
                        room_list = room_list.all().filter(Q(name__contains = phrase) | Q(about__contains = phrase))
        
        
        rooms = room_list
        paginator = Paginator(room_list, 3) # Show 3 rooms per page

        page = request.GET.get('page')
        try:
                rooms = paginator.page(page)
        except PageNotAnInteger:
                rooms = paginator.page(1)
        except EmptyPage:
                rooms = paginator.page(paginator.num_pages)
   
        return render(request, 'room_list.html', {"rooms": rooms, "phrase": phrase, "sort": sort}) 

