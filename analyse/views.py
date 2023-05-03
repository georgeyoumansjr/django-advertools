from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from advertools import url_to_df
from .forms import AnalyseUrls
import pandas as pd



def analyseUrl(request):
    if request.method == 'POST':
        form = AnalyseUrls(request.POST)
        if form.is_valid():
            
            urls = form.cleaned_data['urls']
            urls = list(map(str.strip,urls.split("\n")))

            decode = form.cleaned_data['decode']
            
            df = url_to_df(urls=urls,decode=decode)

            return render(request,'analyse/anUrl.html',{'form': form,'urlsDf': df.to_html(classes='table table-striped text-center', justify='center')})

    else:
        form = AnalyseUrls()
        return render(request,'analyse/anUrl.html',{'form': form})
