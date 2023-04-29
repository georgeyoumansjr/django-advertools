from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from advertools import ad_create


def generateAds(request):
    return render(request, "generateAds/advertisement.html",)


def generate(request, products=['jack'],max_length=100,fallback='Great Cities'):
    if request.is_ajax() and request.method == "POST":
        template = json.loads(request.POST.get('template'))
        products = json.loads(request.POST.get('products'))
        ads_gen = ad_create(template=template,
                replacements=products,
                max_len=30,
                fallback='Great Cities')
        return JsonResponse(
            {
                "success":True,
                "result": ads_gen 
            }
        )
    else:
        return JsonResponse(
            {
                "sucess":False,
                "result": "Invalid request" 
            }
        )




