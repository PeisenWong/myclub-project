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
]