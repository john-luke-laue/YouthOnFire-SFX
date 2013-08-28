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
				return simplejson.dumps({'status':'already'}) 
			emailInstance.save()
			return simplejson.dumps({'status':'Success!'})


	except Exception as e:
		print e
	print "end------"
	return simplejson.dumps({'status':newEmailForm.errors})




@dajaxice_register
def send_message(req, form):
    f = ContactForm(form)
    if f.is_valid():
        # Use mail_admin or something to send off the data like you normally would.
        return simplejson.dumps({'status':'Success!'})
    return simplejson.dumps({'status':f.errors})