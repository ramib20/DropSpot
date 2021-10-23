from django.conf import settings
from twilio.rest import Client

def send_message(receiving_phone_num=0, lat="33.762003", long="-84.416305"):
  print(receiving_phone_num)
  partialURL = 'www.google.com/maps/place/'

  client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
  URL = partialURL + lat + ", " + long
  
  try:
    message = client.messages.create(
      body = "[Hello, this is a notification from {company name}. You will find your package at the following location.] " + URL,
      from_ = '+13204002803',
      to = receiving_phone_num
    )
    print(message)
  except:
    

  