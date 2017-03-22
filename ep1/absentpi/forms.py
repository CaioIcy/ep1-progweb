from django import forms
from .models import Entry

class EntryForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()

    def save(self):
        entry = Entry(text=self.cleaned_data['text'], 
                            language=self.cleaned_data['language'], 
                            title=self.cleaned_data['title'], 
                            name=self.cleaned_data['name'])
        entry.save()
        return entry

