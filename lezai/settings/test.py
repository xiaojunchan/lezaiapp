# -*- coding: utf-8 -*-
from lezai.settings.base import *

TESTING = True
BCRYPT_LOG_ROUNDS = 4 # Use the minimum number of rounds for fast tests
SQLALCHEMY_DATABASE_URI = 'sqlite:///'
CSRF_ENABLED = False
