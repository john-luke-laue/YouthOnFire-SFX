from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from django.template import RequestContext

from main.models import Emails
from main.models import Events

def index(request):
	if request.method == "POST":
		if 'Join' in request.POST:
			addEmail(request)

	return render(request, 'main/index.html')

def addEmail(request):
	post_values = request.POST.copy()
	newEmail = Emails()
	newEmail.email = post_values['email'].strip()
	newEmail.first_name = post_values['fname'].strip()
	newEmail.last_name = post_values['lname'].strip()
	dbNewEmail = newEmail.save()


def about(request):
	return render(request, 'main/about.html')

def events(request):
	latest_events_list = Events.objects.all().order_by('-event_date')[:5]
	return render(request, 'main/events.html', {'latest_events_list': latest_events_list}, context_instance=RequestContext(request))







