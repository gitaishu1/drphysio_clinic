from django import forms

from .models import occupation_model
class occupationform(forms.ModelForm):
    class Meta:
        model=occupation_model
        fields=('occupation',)