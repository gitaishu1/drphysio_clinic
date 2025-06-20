from django import forms

from .models import complaint_model
class complaintform(forms.ModelForm):
    class Meta:
        model=complaint_model
        fields=('complaint','name',)