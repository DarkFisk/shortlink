from django import forms
from django.core.validators import URLValidator
from tracking.models import Link


class CreateLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url']

    def clean_url(self):
        URLValidator(self.cleaned_data['url'])
        return self.cleaned_data['url']
