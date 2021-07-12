from django.contrib import admin
from .models import Venue, MyClubUser, Event

# Register your models here.

# admin.site.register(Venue)
admin.site.register(MyClubUser)
# admin.site.register(Event)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'phone') # State different columns of venues in admin site
	ordering = ('name',) # Ordering of venues created
	search_fields = ('name', 'address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	fields = (('name','venue'), 'event_date', 'description', 'manager', 'attendees') # Change the fields in the admin site
	list_display = ('name', 'event_date', 'venue')
	list_filter = ('event_date', 'venue')
	ordering = ('event_date',)
