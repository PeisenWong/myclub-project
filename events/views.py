from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponse

# Create your views here.


def event_text(request):
	response = HttpResponse(content_type = 'text/plain' )
	response['Content-Disposition'] = 'attachment ; filename = event.txt'

	events = Event.objects.all()
	lines = []

	for event in events:
		lines.append(f'{event.name}\n{event.event_date}\n{event.venue}\n{event.manager}\n{event.description}\n\n\n' )

	response.writelines(lines)
	return response


def venue_text(request):
	response = HttpResponse(content_type = 'text/plain')
	response['Content-Disposition'] = 'attachment ; filename = venues.txt'

	# Designate the model
	venues = Venue.objects.all()
	lines = []
	# Loop through and output
	for venue in venues:
		lines.append(f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n{venue.email_address}\n\n')

	# lines = ['This is line 1 \n',
	# 'This is line 2 \n',
	# 'This is line 3']

	# Write to textfiles
	response.writelines(lines)
	return response


def delete_venue(request, venue_id):
	venue = Venue.objects.get(pk = venue_id)
	venue.delete()
	return redirect('venues-list')

def delete_event(request, event_id):
	event = Event.objects.get(pk = event_id)
	event.delete()
	return redirect('event-list')


def update_event(request, event_id):
	event = Event.objects.get(pk= event_id)
	form = EventForm(request.POST or None ,instance= event) # Instance shows the initial values of the form
	if form.is_valid():
		form.save()
		return redirect('event-list')
	context= {
		'event':event,
		'form':form,
	}
	return render(request, 'events/update_event.html', context)


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
	venues_list = Venue.objects.all().order_by('name') # can filter with all fields in the model
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
	event_list = Event.objects.all().order_by('event_date')
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