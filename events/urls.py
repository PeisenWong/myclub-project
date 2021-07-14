from django.urls import path
from . import views

# Path Converter:
	# int: numbers
	# str: strings
	# path: whole urls /
	# slug: hyphen- and underscores_stuff
	# UUID: universally unique identifier


urlpatterns = [
	path('', views.home, name='home'),
	path('<int:year>/<str:month>', views.home, name='home'),
	path('events', views.all_events, name= 'event-list'),
	path('add_venue', views.add_venue, name= 'add-venue'),
	path('venues', views.venues_list, name= 'venues-list'),
	path('show_venues/<venues_id>', views.show_venues, name= 'show-venues'),
	path('search_venues', views.search_venues, name='search-venues'),
	path('update_venues/<venues_id>', views.update_venues, name='update-venues'),
	path('add_event', views.add_event, name= 'add-event'),
	path('update_event/<event_id>', views.update_event, name='update-event'),
	path('delete_event/<event_id>', views.delete_event, name='delete-event'),
	path('delete_venue/<venue_id>', views.delete_venue, name='delete-venue'),
	path('venue_text', views.venue_text, name= 'venue-text'),
	path('event_text',views.event_text, name = 'event-text')
]