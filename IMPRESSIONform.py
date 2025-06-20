from django import forms

from .models import IMPRESSION_model
class IMPRESSIONform(forms.ModelForm):
    class Meta:
        model=IMPRESSION_model
        fields=('summary','provisionaldiagnos',)