from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LargeScaleAds(forms.Form):
    pass


class GenerateKeywords(forms.Form):
    products = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 30}),)
    word = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 30}),)

    def __init__(self, *args, **kwargs):
        super(GenerateKeywords, self).__init__(*args, **kwargs)
        self.fields['products'].help_text = 'Please add the Input seperated by "," '
        self.fields['word'].help_text = 'Please add the Input seperated by "," '
        self.helper = FormHelper()
        self.helper.add_input(Submit('Generate KeyWords', 'Generate Keywords', css_class='btn-secondary'))
        self.helper.form_method = 'POST'
        


