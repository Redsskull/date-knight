from django import forms

from .models import DateIdea


class DateIdeaForm(forms.ModelForm):
    class Meta:
        model = DateIdea
        fields = 'budget', 'place', 'preferences'
        widgets = {
            "preferences": forms.CheckboxSelectMultiple
        }