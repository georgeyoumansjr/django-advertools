from django.urls import path,include
from . import views

urlpatterns = [
    path("advertisement/",views.generateAds, name='advertisement')

]