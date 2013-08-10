from django.http import HttpResponse
from django.shortcuts import render

from main.models import Emails

def index(request):
	if request.method == "POST":
		if 'Join' in request.POST:
			addEmail(request)

	return render(request, 'main/index.html')

def addEmail(request):
	post_values = request.POST.copy()
	post_values['email'] = post_values['email'].strip()
	newEmail = Emails()
	newEmail.email = post_values['email']
	dbNewEmail = newEmail.save()