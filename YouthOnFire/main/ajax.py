from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

from main.models import EmailForm
from main.models import Email

@dajaxice_register
def sayhello(request):
    return simplejson.dumps({'message':'Hello World!!!ajax.py'})


@dajaxice_register
def submit_email(request, form):
	try:
		newEmailForm = EmailForm(form)
		

		if(newEmailForm.is_valid):
			emailInstance = newEmailForm.save(commit=False)
			if(Email.objects.filter(email=emailInstance.email).count() >= 1):
				return simplejson.dumps({'status':'Hmmm, we already have that email address in our records...'}) 
			emailInstance.save()
			message = emailInstance.first_name + ', we\'ve added your information to our records. Thanks for joining!'
			return simplejson.dumps({'status':message})


	except Exception as e:
		print e

	return simplejson.dumps({'status':'Hmmm, we can\'t seem to save your information. Have you left anything blank? Did you use a valid email address?'})




@dajaxice_register
def send_message(req, form):
    f = ContactForm(form)
    if f.is_valid():
        # Use mail_admin or something to send off the data like you normally would.
        return simplejson.dumps({'status':'Success!'})
    return simplejson.dumps({'status':f.errors})