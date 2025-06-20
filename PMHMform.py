from django import forms

from .models import PMHM_model
class PMHMform(forms.ModelForm):
    class Meta:
        model=PMHM_model
        fields=('rmc','surgeries','Injuries','medications')