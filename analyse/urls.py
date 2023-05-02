from django.urls import path,include
from . import views

urlpatterns = [
    path("urls/",views.analyseUrl, name='anUrl'),
]