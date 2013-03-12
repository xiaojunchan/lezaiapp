# Example ``lz.settings.site`` settings file
from lezai.settings.base import *

# Change the secret key, of course
SECRET_KEY = '\xe6?gT\xd8\xdd\xd8e\xc7\x02\xd5Q&\xe3\xeb\x88\xb6\xf5EP\xc3<\xbc\xec\xd3\t\xa6d@\x0f\xccE\xe2\xaclP'
SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost:5432/lezai'
DEBUG_TB_INTERCEPT_REDIRECTS = False

CONTACT_EMAIL_SENDER = u'webmaster@example.com'
CONTACT_EMAIL_RECIPIENTS = [u'me@example.com']

MAIL_SERVER = 'smtp.example.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'username'
MAIL_PASSWORD = 'password'

SENTRY_DSN = 'https://'
