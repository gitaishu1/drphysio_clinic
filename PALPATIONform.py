from django import forms

from .models import PALPATION_model
class PALPATIONform(forms.ModelForm):
    class Meta:
        model=PALPATION_model
        fields=('tenderness','swelling','muscletone')