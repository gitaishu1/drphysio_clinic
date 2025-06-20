from django import forms

from .models import SPTE_model
class SPTEform(forms.ModelForm):
    class Meta:
        model=SPTE_model
        fields=('testname',)