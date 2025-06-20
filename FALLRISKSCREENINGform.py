from django import forms

from .models import FALLRISKSCREENING_model

class FALLRISKSCREENINGform(forms.ModelForm):
    class Meta:
        model=FALLRISKSCREENING_model
        fields=('criteriatype',)