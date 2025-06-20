from django import forms

from .models import DIAGNOS_model
class DIAGNOSform(forms.ModelForm):
    class Meta:
        model=DIAGNOS_model
        fields=('Xrays','MRI','CT','lab',)