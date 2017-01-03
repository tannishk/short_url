#__author__ = 'sudhir'

from django import forms
from short_url.models import One

class OneForm(forms.ModelForm):
    absolute_url = forms.CharField(max_length=200,help_text='Please enter the URL')
    class Meta:
        model = One
        fields = ['absolute_url']