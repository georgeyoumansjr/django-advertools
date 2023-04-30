from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from advertools import ad_create, kw_generate
from .forms import GenerateKeywords


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


