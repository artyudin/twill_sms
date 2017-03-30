from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml import Response

@csrf_exempt 
def sms(request):
	twiml = '<Response><Message>HYU Hello from your Django app!</Message></Response>'
	return HttpResponse(twiml, content_type='text/xml')
