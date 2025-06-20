from django import forms
from . models import patient_model
gender_choices=[('M','Male'),('F','Female'),('T','Transgender')]

class DateInput(forms.DateInput):
    input_type='date'

class patientform(forms.ModelForm):
    gender=forms.CharField(widget=forms.RadioSelect(choices=gender_choices))
    dob=forms.DateField(widget=DateInput)

    class Meta:
        model=patient_model
        fields=('name','age','gender','dob','mob','occupation','regno','regdate','Docname')