from django.db import models
from django.forms import ModelForm


class Email(models.Model):
	email = models.EmailField()
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	date_added = models.DateTimeField(auto_now_add=True)


	def __unicode__(self):
		return self.email

class EmailForm(ModelForm):
    class Meta:
        model = Email
    	fields = ['email', 'first_name', 'last_name']

class Event(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=8000)
	location = models.CharField(max_length=100)
	pictureFile = models.CharField(max_length=50)
	event_date = models.DateTimeField()
	date_created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title