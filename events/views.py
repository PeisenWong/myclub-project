from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from .forms import VenueForm, EventForm
# Create your views here.


def add_event(request):
	submitted = False # Variable created to state whether user submit the form
	if request.method == 'POST': # If user submit the form
		form = EventForm(request.POST) # Pass the value of the form written by user to the form
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_event?submitted=True') # Pass the submitted variable to the url
	else: # User just came into the form page		
		form = EventForm
		if 'submitted' in request.GET: # User submit the form (Get the submitted)
			submitted= True
	context= {
		'form':form,
		'submitted':submitted
	}
	return render(request, 'events/add_event.html', context)


def update_venues(request, venues_id):
	venue = Venue.objects.get(pk= venues_id)
	form = VenueForm(request.POST or None ,instance= venue) # Instance shws the initial values of the form
	if form.is_valid():
		form.save()
		return redirect('venues-list')
	context= {
		'venue':venue,
		'form':form,
	}
	return render(request, 'events/update_venue.html', context)

def search_venues(request):
	if request.method == 'POST':
		searched = request.POST.get('searched')# Get what did the user searched in the search bar
		venues = Venue.objects.filter(name__contains = searched)
		context = {
			'searched': searched,
			'venues': venues,
		}
		return render(request, 'events/search_venues.html', context)
	else:
		return render(request, 'events/search_venues.html', {})

def show_venues(request, venues_id):
	venue = Venue.objects.get(pk= venues_id)
	context = {
		'venue':venue
	}
	return render(request, 'events/show_venue.html', context)


def venues_list(request):
	venues_list = Venue.objects.all()
	context = {
		'venues_list':venues_list
	}
	return render(request, 'events/venues_list.html', context)

def add_venue(request):
	submitted = False # Variable created to state whether user submit the form
	if request.method == 'POST': # If user submit the form
		form = VenueForm(request.POST) # Pass the value of the form written by user to the form
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_venue?submitted=True') # Pass the submitted variable to the url
	else: # User just came into the form page		
		form = VenueForm
		if 'submitted' in request.GET: # User submit the form (Get the submitted)
			submitted= True

	context= {
		'form':form,
		'submitted':submitted
	}
	return render(request, 'events/add_venue.html', context)

def all_events(request):
	event_list = Event.objects.all()
	context = {
		'event_list':event_list
	}
	return render(request, 'events/event_list.html', context)

def home(request, year= datetime.now().year, month= datetime.now().strftime('%B')): #%B stands for months
	name = 'Kenny'
	month = month.capitalize() # Titlize the first capital of month
	# Convert month from name to number
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)

	# Create a calendar
	cal = HTMLCalendar().formatmonth(year, month_number)

	# Get current year
	now = datetime.now()
	current_year = now.year

	# Get current time
	time = now.strftime('%I:%M %p') # If use %H instead of %I , it will be 15:00 in 3pm , # %p will show am or pm

	context = {
	'name': name,
	'year': year,
	'month': month,
	'month_number': month_number, 
	'cal' : cal,
	'current_year': current_year,
	'time': time
	}
	return render(request, 'events/home.html', context)