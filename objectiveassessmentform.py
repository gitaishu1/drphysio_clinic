from django import forms

from .models import objectiveassessment_model
class objectiveassessmentform(forms.ModelForm):
    class Meta:
        model=objectiveassessment_model
        fields=('postureandmovement',)