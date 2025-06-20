from django import forms

from .models import FUNCTIONLIM_model
class FUNLIMform(forms.ModelForm):
    class Meta:
        model=FUNCTIONLIM_model
        fields=('assessmentofcondition','activitiesofdailyiving',)