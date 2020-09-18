from django import forms

from shortener.models import URL


class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['full_url', 'url_hash', ]
