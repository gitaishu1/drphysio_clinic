from django import forms

from .models import cervicalspinemotion_model
class cervicalspinemotionform(forms.ModelForm):
    class Meta:
        model=cervicalspinemotion_model
        fields=('motionname','typename',)