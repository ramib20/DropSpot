from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.conf import settings
from .models import Delivery
from .serializer import DeliverySerializer
from django.views.decorators.csrf import csrf_exempt
from .auxiliary import send_message

import requests
import os
from twilio.rest import Client

@csrf_exempt # temp solution for testing
def location(request):
  print(request.POST)

  if request.method == "GET":
    return render(request, 'index.html')
    
    phone_num, lat, long = 0
    
    # request method is POST:
    response = send_message(phone_num, lat, long)

  return HttpResponse(response)
  #HttpResponse("location got")

# @csrf_exempt # temp solution for testing
# def send_message(request, receiving_phone_num=0, coordinates = "33.762003,-84.416305"):
#   if request.method == "GET":
#     return render(request, 'index.html')
  
#   # request method is POST:
#   print(receiving_phone_num)
#   partialURL = 'www.google.com/maps/place/'

#   client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
#   URL = partialURL + coordinates
  
#   message = client.messages.create(
#     body = "[Hello, this is a notification from {company name}. You will find your package at the following location.] " + URL,
#     from_ = '+13204002803',
#     to = receiving_phone_num
#   )
#   print(message)
#   # call apis

#   return HttpResponse(request, "message sent")

# def send_address()


def display_form(request):
  return render(request, 'index.html')


