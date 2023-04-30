from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LargeScaleAds(forms.Form):
    pass


class GenerateKeywords(forms.Form):
    product = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, 
    "cols": 30,
    'placeholder':'Enter the products you want to generate keywords for seperated by "," like\nshoes,shirt,scarf'
    }
    ))
    word = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, 
    "cols": 30,
    'placeholder':'Enter the words you want to generate keywords for seperated by "," like\nbuy,cheap,quality,premium'
    }
    ))

    def __init__(self, *args, **kwargs):
        super(GenerateKeywords, self).__init__(*args, **kwargs)
        self.fields['product'].help_text = 'Please add the Input seperated by "," '
        self.fields['word'].help_text = 'Please add the Input seperated by "," '
        # self.fields['products'].widget.attrs['placeholder'] = 'Enter the products you want to generate keywords for seperated by "," like\nshoes,shirt,scarf'
        # self.fields['word'].widget.attrs['placeholder'] = 'Enter the words you want to generate keywords for seperated by "," like\nbuy,cheap,quality,premium'
        self.helper = FormHelper()
        self.helper.add_input(Submit('Generate KeyWords', 'Generate Keywords', css_class='btn-secondary'))
        self.helper.form_method = 'POST'
        


