from django import forms

from .models import PHYSIOGOALS_model
class PHYSIOGOALSform(forms.ModelForm):
    class Meta:
        model=PHYSIOGOALS_model
        fields=('shorttermgoals','longtermgoals',)