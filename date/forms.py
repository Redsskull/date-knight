from django import forms
from .models import DateIdea

class DateIdeaForm(forms.ModelForm):
    class Meta:
        model = DateIdea
        fields = ['budget', 'place', 'time']
        widgets = {
            'budget': forms.RadioSelect,
            'place': forms.RadioSelect,
            'time': forms.RadioSelect,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['budget'].empty_label = None
        self.fields['place'].empty_label = None
        self.fields['time'].empty_label = None