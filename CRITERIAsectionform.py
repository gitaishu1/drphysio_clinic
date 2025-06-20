from django import forms

from .models import CRITERIAsection_model
class CRITERIAsectionform(forms.ModelForm):
    class Meta:
        model=CRITERIAsection_model
        fields=('criteriatype','sectionname',)