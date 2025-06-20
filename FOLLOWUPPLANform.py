from django import forms

from .models import FOLLOWUPPLAN_model
class FOLLOWUPPLANform(forms.ModelForm):
    class Meta:
        model=FOLLOWUPPLAN_model
        fields=('frequencyofvisits','reassessment','modifications')