from django import forms
from .models import LyricInsert

class LyricInsertForm(forms.ModelForm):
    class Meta:
        model=LyricInsert
        fields=('lyric_candidate',)