from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from advertools import ad_create, kw_generate, ad_from_string
from .forms import GenerateKeywords, LargeScaleAds

import pandas as pd


def generateLarge(request):
    if request.method == 'POST':
        form = LargeScaleAds(request.POST)
        if form.is_valid():
            
            description_text = form.cleaned_data['description_text']
            slots = form.cleaned_data['slots']
            # print(slots)
            if slots:
                slots = list(map(str.strip,slots.split(",")))
                slots = list(map(float,slots))
                generateLargeAds = ad_from_string(description_text, slots=slots)
            else:
                slots = None
                generateLargeAds = generateLargeAds = ad_from_string(description_text)

            df = pd.DataFrame({
                'large_ads': generateLargeAds
            })

            return render(request,'generateAds/advertisement.html',{'form': form,'adsDf': df.to_html(classes='table table-striped text-center', justify='center')})

    else:
        form = LargeScaleAds()
        return render(request,'generateAds/advertisement.html',{'form': form})


def generateLarge(request):
    if request.method == 'POST':
        form = LargeScaleAds(request.POST)
        if form.is_valid():
            
            description_text = form.cleaned_data['description_text']
            slots = form.cleaned_data['slots']
            # print(slots)
            if slots:
                slots = list(map(str.strip,slots.split(",")))
                slots = list(map(float,slots))
                generateLargeAds = ad_from_string(description_text, slots=slots,capitalize=True)
            else:
                slots = None
                generateLargeAds = generateLargeAds = ad_from_string(description_text,capitalize=True)

            df = pd.DataFrame({
                'large_ads': generateLargeAds
            })

            return render(request,'generateAds/advertisement.html',{'form': form,'adsDf': df.to_html(classes='table table-striped text-center', justify='center')})

    else:
        form = LargeScaleAds()
        return render(request,'generateAds/advertisement.html',{'form': form})


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


def generateKeywords(request):
    if request.method == 'POST':
        form = GenerateKeywords(request.POST)
        if form.is_valid():
            
            product = form.cleaned_data['product']
            word = form.cleaned_data['word']
            products = list(map(str.strip,product.split(",")))
            words = list(map(str.strip,word.split(",")))

            keywordDf = kw_generate(products,words)

            return render(request,'generateAds/keywords.html',{'form': form,'keywordDf': keywordDf.to_html(classes='table table-striped text-center', justify='center')})

    else:
        form = GenerateKeywords()
        return render(request,'generateAds/keywords.html',{'form': form})


