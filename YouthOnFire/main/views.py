from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from django.template import RequestContext

from main.models import Email
from main.models import Event

import datetime
from datetime import date  


from django.utils import simplejson
from dajaxice.decorators import dajaxice_register


@dajaxice_register
def sayhello(request):
    return simplejson.dumps({'message':'Hello World'})



def index(request):
	if request.method == "POST":
		if 'Join' in request.POST:
			addEmail(request)

	return render(request, 'main/index.html')

def addEmail(request):
	post_values = request.POST.copy()
	newEmail = Email()
	newEmail.email = post_values['email'].strip()
	newEmail.first_name = post_values['fname'].strip()
	newEmail.last_name = post_values['lname'].strip()
	dbNewEmail = newEmail.save()

def calendar(request):
	return render(request, 'main/calendar.html')

def events(request):
	start_date = date.today()
	end_date = datetime.date(2050, 12, 31)
	latest_events_list = Event.objects.filter(event_date__range=(start_date, end_date)).order_by('event_date')[:5]
	return render(request, 'main/events.html', {'latest_events_list': latest_events_list}, context_instance=RequestContext(request))







