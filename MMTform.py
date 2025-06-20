from django import forms

from .models import MMT_model
class MMTform(forms.ModelForm):
    class Meta:
        model=MMT_model
        fields=('typename',)
