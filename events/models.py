from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
	name =models.CharField('Venue Name', max_length=120) 
	address = models.CharField(max_length=300)
	zip_code =models.CharField(max_length=15)
	phone = models.CharField(max_length=25, blank =True)
	web = models.URLField('Website Address', blank =True)
	email_address = models.EmailField('Email Address', blank =True)

	def __str__(self):    # Show the name of object created in admin site
		return self.name

class MyClubUser(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email = models.EmailField('User Email')

	def __str__(self):
		return self.first_name + ' ' + self.last_name

class Event(models.Model):
	name        = models.CharField('Event Name', max_length = 120)
	event_date  = models.DateTimeField('Event Date')
	#venue       = models.CharField(max_length = 120)							# CASCADE function will delete all the things(Venue in this case) when one Event is deleted
	venue       = models.ForeignKey(Venue, blank=True, null = True, on_delete= models.CASCADE)  # Connect the venue table into Event table
	manager     = models.ForeignKey(User, blank = True, null = True, on_delete = models.SET_NULL) # When the manager delete his profile, other event managed by him will be invalid(null)
	description = models.TextField(blank=True)
	attendees   = models.ManyToManyField(MyClubUser, blank = True)

	def __str__(self):
		return self.name