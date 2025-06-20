from django import forms

from .models import TOTALSCORE_model
class TOTALSCOREform(forms.ModelForm):
    class Meta:
        model=TOTALSCORE_model
        fields=('range',)