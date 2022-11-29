import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
PHONE_FROM= os.getenv('TWILIO_PHONE_FROM')
PHONE_TO= os.getenv('TWILIO_PHONE_TO')