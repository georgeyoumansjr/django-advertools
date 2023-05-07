from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from advertools import robotstxt_to_df, sitemap_to_df, serp_goog, knowledge_graph
from .forms import RobotsTxt, Sitemap, SerpGoogle, KnowledgeG
from decouple import config


import pandas as pd
pd.set_option('display.max_colwidth', 30)

def robotsToDf(request):
    if request.method == 'POST':
        form = RobotsTxt(request.POST)
        if form.is_valid():
            
            urls = form.cleaned_data['urls']

            urls = list(map(str.strip,urls.split("\n")))
            df = robotstxt_to_df(urls)
           
            return render(request,'seo/robots.html',{'form': form,'roboDf': df.to_html(classes='table table-striped text-center', justify='center')})

    else:
        form = RobotsTxt()
        return render(request,'seo/robots.html',{'form': form})

def sitemapToDf(request):
    if request.method == 'POST':
        form = Sitemap(request.POST)
        if form.is_valid():
            
            urls = form.cleaned_data['urls']

            # urls = list(map(str.strip,urls.split("\n")))
            df = sitemap_to_df(urls)
           
            return render(request,'seo/sitemap.html',{'form': form,'siteDf': df.to_html(col_space='75px',classes='table table-striped text-center', justify='center')})

    else:
        form = Sitemap()
        return render(request,'seo/sitemap.html',{'form': form})



def searchEngineResults(request):
    if request.method == 'POST':
        form = SerpGoogle(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            query = list(map(str.strip,query.split(",")))
            gl = form.cleaned_data['geolocation']
            print(gl)
            # gl = list(map(str.strip,gl.split(",")))
            country = form.cleaned_data['country']
            country = list(map(str.strip,country.split(","))) if country else None
            serpDf = serp_goog(q=query,cx=config('CX'),key=config('KEY'),gl=gl,cr=country)
            return render(request,'seo/serpGoog.html',{'form': form,'serpDf':serpDf.to_html(classes='table table-striped text-center', justify='center')})

    else:
        form = SerpGoogle()
        return render(request, 'seo/serpGoog.html',{'form': form})
    


def knowledgeGraph(request):
    if request.method == 'POST':
        form = KnowledgeG(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            query = list(map(str.strip,query.split(",")))
            languages = form.cleaned_data['languages']
            
            languages = list(map(str.strip,languages.split(",")))if languages else None
            
            knowDf = knowledge_graph(query=query,key=config('KEY'),languages=languages)
            return render(request,'seo/knowledgeG.html',{'form': form,'knowDf':knowDf.to_html(classes='table table-striped text-center', justify='center')})

    else:
        form = KnowledgeG()
        return render(request, 'seo/knowledgeG.html',{'form': form})

