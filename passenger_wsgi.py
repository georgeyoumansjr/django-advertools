import imp
import os 
import sys 

sys.path.insert(0, os.path.dirname(__file___))

wsgi = imp.load_source('wsgi', 'django_advertools/wsgi.py')
application = wsgi.application