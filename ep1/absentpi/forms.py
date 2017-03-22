from django import forms
from .models import Entry

class EntryForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 20, 'cols': 80}))

    def save(self):
        entry = Entry(text=self.cleaned_data['text'],
                      title=self.cleaned_data['title'])
        entry.save()
        return entry

