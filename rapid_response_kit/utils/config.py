try:
   import local_config
except:
    try:
      import os
      SECRET_KEY = os.environ['SECRET_KEY']
      TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
      TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
      GOOGLE_ACCOUNT_USER = os.environ['GOOGLE_ACCOUNT_USER']
      GOOGLE_ACCOUNT_PASS = os.environ['GOOGLE_ACCOUNT_PASS']
      PUSHER_APP_ID = os.environ['PUSHER_APP_ID']
      PUSHER_KEY = os.environ['PUSHER_KEY']
      PUSHER_SECRET = os.environ['PUSHER_SECRET']
      FIREBASE_URL = os.environ['Application ID']
      FIREBASE_SECRET = os.environ['REST API key']
    except:
        pass


# Configuration Auto-generated during installation
SECRET_KEY = '\xdb\xd7\xed\\HL\xd1\x08\xdc\xe7\xd0\x8c"\x12\x9b\xc8)\xe8\x7f;'
TWILIO_ACCOUNT_SID = 'AC24333f9717e4958f7c9fafa2f755b802'
TWILIO_AUTH_TOKEN = 'f845fd097c210512128658fdedcb6a00'

# Configuration Auto-generated during installation
SECRET_KEY = b'8.za\xa3jH\xfd[\xb9y\x19Y\x12\xc5\xee?8z\xe1'
TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''

# Configuration Auto-generated during installation
SECRET_KEY = b';\xa6\xa3t[\x04Y\xcd\t\x9b\x9b\xa8|4J\x19t\x00HK'
TWILIO_ACCOUNT_SID = 'AC24333f9717e4958f7c9fafa2f755b802'
TWILIO_AUTH_TOKEN = 'f845fd097c210512128658fdedcb6a00'