from django.urls import path,include
from . import views

urlpatterns = [
    path("advertisement/",views.generateLarge, name='advertisement'),
    path("keywords/",views.generateKeywords, name='keywords')

]