from clint.textui import colored
import os

print()
print()
print(colored.red(" --- Enter your Twilio information below to complete install --- "))
print()
print()

account_sid = input('Twilio Account Sid: ')
auth_token = input('Twilio Auth Token: ')

config = """\n\n# Configuration Auto-generated during installation
SECRET_KEY = {}
TWILIO_ACCOUNT_SID = '{}'
TWILIO_AUTH_TOKEN = '{}'""".format(repr(os.urandom(20)), account_sid, auth_token)

f = open('rapid_response_kit/utils/config.py', 'r')
contents = f.read()
f.close()
f = open('rapid_response_kit/utils/config.py', 'w')
f.write(contents + config)
f.close()

print()
print()
print(colored.red(" --- Would you like to add other credentials now? ---"))
print()
print()

decision = input("Type 'yes' or 'no': ")

if decision == 'yes':
    firebase_url = input('Firebase Url (optional): ')
    firebase_secret = input('Firebase Secret Key (optional): ')
    pusher_app_id = input('Pusher App ID (optional): ')
    pusher_key = input('Pusher Key (optional): ')
    pusher_secret = input('Pusher Secret (optional): ')
    google_user = input('Google email (optional): ')
    google_pass = input('Google password (optional): ')

    new_config = '''
GOOGLE_ACCOUNT_USER = '{}'
GOOGLE_ACCOUNT_PASS = '{}'
PUSHER_APP_ID = '{}'
PUSHER_KEY = '{}'
PUSHER_SECRET = '{}'
FIREBASE_URL = '{}'
FIREBASE_SECRET = '{}'
    '''.format(
        google_user,
        google_pass,
        pusher_app_id,
        pusher_key,
        pusher_secret,
        firebase_url,
        firebase_secret)

    f = open('rapid_response_kit/utils/config.py', 'r')
    contents = f.read()
    f.close()
    f = open('rapid_response_kit/utils/config.py', 'w')
    f.write(contents + new_config)
    f.close()
