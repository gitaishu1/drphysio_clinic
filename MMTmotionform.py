from django import forms

from .models import MMTmotion_model
class MMTmotionform(forms.ModelForm):
    class Meta:
        model=MMTmotion_model
        fields=('typename','motionname',)