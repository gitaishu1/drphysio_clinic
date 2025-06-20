from django import forms

from .models import SocialHistory_model
class socialhistoryform(forms.ModelForm):
    class Meta:
        model=SocialHistory_model
        fields=('lifestyle','activitylevels','habits','healthissues')