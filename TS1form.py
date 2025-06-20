from django import forms

from .models import TS1_model
class TS1form(forms.ModelForm):
    class Meta:
        model=TS1_model
        fields=('name','range','risk','facility',)