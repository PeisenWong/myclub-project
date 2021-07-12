from django import forms
from django.forms import ModelForm
from .models import Venue

# Create a venue form
class VenueForm(ModelForm):
	class Meta:
		model = Venue
		fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
		labels={
		'name':'' , # Change the label here
		'address':'' ,
		'zip_code':'' ,
		'phone':'' ,
		'web':'' ,
		'email_address':'' ,
		}
		widgets = {
		'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name' }),
		'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address', 'rows':50, 'col':120 }),
		'zip_code':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code' }),
		'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone number' }),
		'web':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web' }),
		'email_address':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address' }),
		}
