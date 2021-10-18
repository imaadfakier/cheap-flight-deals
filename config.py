import os

# --- sheety api
# sheety http basic authentication
#   username
os.environ['SHEETY_AUTH_USERNAME'] = 'enter auth username'
SHEETY_AUTH_USERNAME = os.environ.get('SHEETY_AUTH_USERNAME')
#   password
os.environ['SHEETY_AUTH_PASSWORD'] = 'enter auth password'
SHEETY_AUTH_PASSWORD = os.environ.get('SHEETY_AUTH_PASSWORD')

# --- kiwi api
os.environ['KIWI_API_KEY'] = 'enter api key'
KIWI_API_KEY = os.environ.get('KIWI_API_KEY')


# --- twilio api
#   account sid
os.environ['TWILIO_ACCOUNT_SID'] = 'enter account sid'
TWILIO_ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
#   authentication token
os.environ['TWILIO_AUTH_TOKEN'] = 'enter auth token'
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

# --- for email notification(s)
os.environ['SMTP_SERVER_ADDRESS'] = 'enter server address'
SMTP_SERVER_ADDRESS = os.environ.get('SMTP_SERVER_ADDRESS')
os.environ['TEST_SENDER_EMAIL'] = 'enter sender email'
TEST_SENDER_EMAIL = os.environ.get('TEST_SENDER_EMAIL')
os.environ['TEST_SENDER_EMAIL_PASSWORD'] = 'enter sender password'
TEST_SENDER_EMAIL_PASSWORD = os.environ.get('TEST_SENDER_EMAIL_PASSWORD')
os.environ['TEST_RECEIVER_EMAIL'] = 'enter receiver email'
TEST_RECEIVER_EMAIL = os.environ.get('TEST_RECEIVER_EMAIL')
