from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from advertools import url_to_df, emoji_search, extract_emoji
from .forms import AnalyseUrls, EmojiSearch, EmojiExtract
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



def searchEmoji(request):
    if request.method == 'POST':
        form = EmojiSearch(request.POST)
        if form.is_valid():
            
            emoji_text = form.cleaned_data['emoji_text']
           
            df = emoji_search(emoji_text)

            return render(request,'analyse/emoji.html',{'form': form,'emojiDf': df.to_html(classes='table table-striped text-center', justify='center')})

    else:
        form = EmojiSearch()
        return render(request,'analyse/emoji.html',{'form': form})


def extractEmoji(request):
    if request.method == 'POST':
        form = EmojiExtract(request.POST)
        if form.is_valid():
            
            emoji_text = form.cleaned_data['emoji_text']
            emoji_text = list(map(str.strip,emoji_text.split("\n")))
            df = extract_emoji(emoji_text)
            # print(df)
            df = pd.DataFrame.from_dict(df,orient='index')
            df = df.transpose()
            return render(request,'analyse/emojiExtract.html',{'form': form,'emojiDf': df.to_html(classes='table table-striped text-center', justify='center')})

    else:
        form = EmojiExtract()
        return render(request,'analyse/emojiExtract.html',{'form': form})




