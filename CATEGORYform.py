from django import forms

from .models import CATEGORY_model

class DateInput(forms.DateInput):
    input_type='date'

class CATEGORYform(forms.ModelForm):
    Date = forms.DateField(widget=DateInput)

    class Meta:
        model=CATEGORY_model
        fields=('criteriatype','sectionname','score','Date',)
