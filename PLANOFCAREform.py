from django import forms

from .models import PLANOFCARE_model
class PLANOFCAREform(forms.ModelForm):
    class Meta:
        model=PLANOFCARE_model
        fields=('treatmentstrategies','modalities','exercises')