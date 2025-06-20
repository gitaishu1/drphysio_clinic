from django import forms

from .models import ROMtype_model


class ROMtypeform(forms.ModelForm):
    class Meta:
        model=ROMtype_model
        fields=('typename',)