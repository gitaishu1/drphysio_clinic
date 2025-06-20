from django import forms

from .models import PATIENTEDUCATION_model
class PATIENTEDUCATIONform(forms.ModelForm):
    class Meta:
        model=PATIENTEDUCATION_model
        fields=('explanationofcondition','prognosis','selfmanagement')