from twilio.rest import Client
from .settings import ACCOUNT_SID, AUTH_TOKEN, PHONE_FROM, PHONE_TO

class Service:
  @staticmethod
  def __init__():   
   pass
  
  @staticmethod
  def run():    
    client = Client(ACCOUNT_SID, AUTH_TOKEN)  
    message = client.messages.create(
      body='Hi there',
      from_=PHONE_FROM,
      to=PHONE_TO
    ) 

    print(message.sid)