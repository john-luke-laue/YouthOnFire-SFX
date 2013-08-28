from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from django.template import RequestContext

from main.models import Email
from main.models import EmailForm
from main.models import Event

import datetime
from datetime import date  


from django.utils import simplejson
from dajaxice.decorators import dajaxice_register


def index(request):
	return render(request, 'main/index.html',  {'form':EmailForm()})


def calendar(request):
	return render(request, 'main/calendar.html')

def events(request):
	start_date = date.today()
	end_date = datetime.date(2050, 12, 31) #a sufficiently far away date
	latest_events_list = Event.objects.filter(event_date__range=(start_date, end_date)).order_by('event_date')[:5] #get the first 5 future events that are closest to today
	return render(request, 'main/events.html', {'latest_events_list': latest_events_list}, context_instance=RequestContext(request))







