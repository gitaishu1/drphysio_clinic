from django import forms

from .models import NEUROASS_model
class NEUROASSform(forms.ModelForm):
    class Meta:
        model=NEUROASS_model
        fields=('reflexes','sensation','nervefunction')