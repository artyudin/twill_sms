from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml import Response

@csrf_exempt 
def sms(request):
	twiml = '<Response><Message>Welcome to Practical Programming, Please go upstairs, third floor, Doorcode is 1212*</Message></Response>'
	return HttpResponse(twiml, content_type='text/xml')
