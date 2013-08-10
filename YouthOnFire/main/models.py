from django.db import models


class Emails(models.Model):
	email = models.CharField(max_length=50, unique=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.email
