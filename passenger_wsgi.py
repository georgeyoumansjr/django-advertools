from django_advertools.asgi import application
from a2wsgi import ASGIMiddleware
application = ASGIMiddleware(application)