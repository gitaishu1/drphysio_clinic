from django import forms

from .models import HPI_model
class HPIform(forms.ModelForm):
    class Meta:
        model=HPI_model
        fields=('onset','current_date','painscore','Duration','POS','Aggr','Relf')