from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect, get_object_or_404

def generateAds(request):
    return render(request, "generateAds/advertisement.html")





