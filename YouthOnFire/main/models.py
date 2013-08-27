from django.db import models


class Emails(models.Model):
	email = models.CharField(max_length=50, unique=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	date_added = models.DateTimeField(auto_now_add=True)


	def __unicode__(self):
		return self.email

class Events(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=8000)
	event_date = models.DateTimeField()
	date_created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title