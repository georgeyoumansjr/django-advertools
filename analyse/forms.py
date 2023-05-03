from django import forms

class AnalyseUrls(forms.Form):
    urls = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, 
    "cols": 40,
    "placeholder": "Enter urls in new lines like  \nhttp://localhost:8000/generate/advertisement/large/\nhttps://importsem.com/create-a-custom-twitter-tweet-alert-system-with-python/"
    }
    ))

    decode = forms.BooleanField(required=False)
