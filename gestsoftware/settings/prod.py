from distutils.debug import DEBUG
import django_on_heroku
from decouple import config
#from gestsoftware.settings.dev import ALLOWED_HOSTS
#from gestsoftware.settings.dev import SECRET_KEY

from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'gestsoftware-cg-herokuapp.com',
]